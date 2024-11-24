import openai
import os
import dotenv
from openai import OpenAI
import json
from structurize import get_question_json

dotenv.load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key


def generate_ged_style_question(system_prompt, user_prompt):
    """
    Generate a GED-style question that asks the user to select a quotation from the passage.
    
    :param text: The input passage text to generate the question from.
    :return: The question with options and the correct answer.
    """
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return completion.choices[0].message.content


def read_prompts(system_prompt_path, user_prompt_path):
    """
    Read the system and user prompts from files.
    """
    with open(system_prompt_path, "r", encoding="utf-8") as system_file:
        system_prompt = system_file.read()
    with open(user_prompt_path, "r", encoding="utf-8") as user_file:
        user_prompt = user_file.read()
    return system_prompt, user_prompt


if __name__ == "__main__":
    # File paths
    system_prompt_path = './prompts/system_prompt.txt'
    user_prompt_path = './prompts/user_prompt.txt'
    output_file = './output/generated_question.json'

    # Read prompts
    system_prompt, user_prompt = read_prompts(system_prompt_path, user_prompt_path)

    # Generate question
    question_string = generate_ged_style_question(system_prompt, user_prompt)
    question_dict = get_question_json(question_string)

    # Save result as JSON
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(question_dict, file, indent=4)

    print(f"Generated question saved to {output_file}:\n")
    print(json.dumps(question_dict, indent=4))

    # print("========")
    # print(question_string)
    # print("========")