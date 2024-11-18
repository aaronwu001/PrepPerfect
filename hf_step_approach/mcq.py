
import requests
import os
import dotenv
import json

# Load environment variables
dotenv.load_dotenv()
HF_TOKEN = os.getenv('HF_TOKEN')

# Correct Inference API URL for the model
API_URL = "https://api-inference.huggingface.co/models/dslim/bert-large-NER"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# Function to query the Hugging Face API
def query_huggingface_api(article_text):
    payload = {
        "inputs": article_text,
        "options": {"wait_for_model": True},
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

if __name__ == '__main__':
    # Read the article from the file
    file_path = "sample_article.txt"  # Replace with your file path
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            article_text = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        exit()

    # Query the Hugging Face API and extract keywords
    try:
        keywords = query_huggingface_api(article_text)
        print("Important Keywords:", keywords)
    except Exception as e:
        print(str(e))
