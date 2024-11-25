import openai
import os
import dotenv
from openai import OpenAI
import pdfplumber
from parse import parse_questions_to_json
import json

# Load environment variables from a .env file
dotenv.load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')


# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    """
    Extracts text content from all pages of a given PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: Combined text from all pages in the PDF.
    """
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text


# Function to use GPT to generate similar questions
def generate_similar_questions(extracted_text, api_key, n_questions=5):
    """
    Generates similar GED-style questions using GPT-4o-mini model.

    Args:
        extracted_text (str): Reference text from the PDF to guide question generation.
        api_key (str): OpenAI API key for authentication.
        n_questions (int): Number of questions to generate.

    Returns:
        str: Generated questions as a formatted string.
    """
    openai.api_key = API_KEY
    prompt = f"""
        You are provided with example GED RLA practice questions below. These questions include various combinations of passage types and question types based on the provided examples. Use these examples to generate new questions that align with the style and diversity of the GED RLA study guide.

        Reference questions:
        {extracted_text}

        Generate exactly {n_questions} new multiple-choice questions, ensuring a balanced distribution:
        - **Half (50%) of the questions should include a passage** and test comprehension, tone, main ideas, or author's purpose. Passages must be 8–10 sentences long, varied, and tied logically to the question.
        - **Half (50%) of the questions should NOT include a passage** and test grammar, language use, or similar skills that do not require a passage.

        Maintain the following strict format for all questions. The response should start with the first line of the first question. The hyphens and start symbols should be strictly identical to the format below. The questions should be seprated by two empty lines and tree hyphens. So between the questions should be (new line) --- (new line)

        - **Question Type:** [Based on the types inferred from the provided examples, specify the question type in this field.]
        - **Question:** [Clearly stated question.]
        - **Passage:** [Include a passage ONLY for the passage-based questions. If the question does not require a passage, set the value for this field to "None". Do not leave it blank or use a placeholder such as "-".]
        - **Options:**
          - A. [Option 1]
          - B. [Option 2]
          - C. [Option 3]
          - D. [Option 4]
        - **Correct Answer:** [Letter of the correct answer, e.g., "B".]
        - **Explanation:** [A concise explanation of why the answer is correct and why the other options are incorrect.]

        **Key Requirements**:
        1. **Balanced Distribution**: Ensure exactly half the questions include a passage, and the other half do not.
        2. **Passage Consistency**: For non-passage-based questions, explicitly set the passage field to "None". Passages must be detailed (8–10 sentences) and relevant to the question for passage-based questions.
        3. **Diverse Question Types**: Include a mix of question types such as main ideas, tone, grammar, and language use, based on examples provided.
        4. **Rigorous Structure**: Follow the format strictly, ensuring logical consistency and completeness for all fields.

        Generate the questions adhering to these guidelines without replicating specific examples from the reference material.
    """

    # Initialize the OpenAI client and request question generation
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content


def generate_mcq_from_sample_question(pdf_path, api_key, n_questions=5):
    """
    Generates multiple-choice questions from a sample question PDF.

    Args:
        pdf_path (str): Path to the input PDF file.
        api_key (str): API key for accessing OpenAI services.
        n_questions (int): Number of questions to generate.

    Returns:
        dict: A dictionary containing the generated questions string and parsed questions.
    """
    # Step 1: Extract text from the PDF
    print("Extracting text from the PDF...")
    extracted_text = extract_text_from_pdf(pdf_path)

    # Step 2: Generate similar questions using GPT
    print("Generating questions using GPT...")
    questions_string = generate_similar_questions(extracted_text, api_key, n_questions)

    # Step 3: Parse the generated questions string into a JSON object
    print("Parsing the generated questions into JSON format...")
    parsed_questions = parse_questions_to_json(questions_string)

    print("Question generation process completed successfully!")
    result = {
        "questions_string": questions_string,
        "parsed_questions": parsed_questions
    }
    return result


# Main Program
if __name__ == '__main__':
    # Specify the path to the input PDF
    pdf_path = "./materials/GED_Study-Guide_RLA.pdf"  # Update with the actual file path
    api_key = API_KEY  # OpenAI API key from environment variables
    n_questions = 5  # Number of questions to generate

    # Generate multiple-choice questions from the PDF
    question_result = generate_mcq_from_sample_question(pdf_path, api_key, n_questions)

    # Extract results
    questions_string = question_result["questions_string"]
    parsed_questions = question_result["parsed_questions"]

    # Create an output directory if it doesn't exist
    output_dir = "./output/"
    os.makedirs(output_dir, exist_ok=True)

    # Define file paths for saving the results
    questions_string_file = os.path.join(output_dir, "questions_string.txt")
    parsed_questions_file = os.path.join(output_dir, "parsed_questions.json")

    # Save the questions string to a text file
    print(f"Saving the questions string to {questions_string_file}...")
    with open(questions_string_file, "w", encoding="utf-8") as qs_file:
        qs_file.write(questions_string)

    # Save the parsed questions to a JSON file
    print(f"Saving the parsed questions to {parsed_questions_file}...")
    with open(parsed_questions_file, "w", encoding="utf-8") as pq_file:
        json.dump(parsed_questions, pq_file, indent=4, ensure_ascii=False)
