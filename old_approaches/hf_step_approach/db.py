from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import random
import os
import dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Load environment variables
dotenv.load_dotenv()
uri = os.getenv('MONGO_URI')

# MongoDB client setup
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.testing_system

# FastAPI setup
app = FastAPI()

# Load BERT model for masked language modeling
fill_mask = pipeline("fill-mask", model="bert-base-uncased")

# Models for request validation
class QuestionRequest(BaseModel):
    user_id: str
    subject: str = "Math"
    topic: str

class AnswerRequest(BaseModel):
    user_id: str
    question_id: str
    answer: str

# Generate MCQ function
def generate_mcq(text, mask_token="[MASK]"):
    key_word = "important"  # Choose a word to mask
    question = text.replace(key_word, mask_token)
    
    # Generate distractor answers
    results = fill_mask(question)
    answers = [result['token_str'] for result in results[:4]]  # Top 4 predictions
    
    # Ensure the correct answer is included
    if key_word not in answers:
        answers[random.randint(0, 3)] = key_word  # Replace a random distractor with the correct answer
    
    random.shuffle(answers)  # Shuffle answers
    
    # Return JSON-compatible MCQ object
    mcq = {
        "question": question.replace(mask_token, "______"),
        "choices": answers,
        "correct_answer": key_word
    }
    return mcq

# FastAPI Routes
@app.post("/generate_question")
async def generate_question(request: QuestionRequest):
    # Generate a question
    text = "The most important factor for success is consistency."  # Sample text
    question_data = generate_mcq(text)
    
    # Insert question data into MongoDB
    result = await db.questions.insert_one(question_data)
    question_data["_id"] = str(result.inserted_id)  # Convert ObjectId to string

    return question_data

@app.post("/submit_answer")
async def submit_answer(answer: AnswerRequest):
    # Retrieve the question from the database
    question = await db.questions.find_one({"_id": answer.question_id})
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    # Check the user's answer
    is_correct = answer.answer == question["correct_answer"]

    # Update the user score in MongoDB
    score = await db.scores.find_one({"user_id": answer.user_id}) or {"score": 0}
    score_update = 2 if is_correct else -1
    new_score = max(0, score["score"] + score_update)  # Prevent negative scores
    await db.scores.update_one({"user_id": answer.user_id}, {"$set": {"score": new_score}}, upsert=True)

    return {"correct": is_correct, "new_score": new_score}

@app.get("/user/{user_id}")
async def get_user_info(user_id: str):
    # Retrieve user's score and topic
    user_score = await db.scores.find_one({"user_id": user_id})
    return {
        "user_id": user_id,
        "score": user_score.get("score", 0),
        "topic": user_topic.get("topic", "Introduction")
    }
