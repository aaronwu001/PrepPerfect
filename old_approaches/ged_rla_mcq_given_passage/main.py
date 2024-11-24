import openai
import os
import dotenv
from openai import OpenAI
dotenv.load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key
from structurize import get_structured_question
import json


def generate_ged_style_question(system_prompt, user_prompt, passage):
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
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return completion.choices[0].message.content


def replace_variable_in_prompt(file_path, variables):
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        prompt = file.read()
    # Replace variables in the prompt
    for key, value in variables.items():
        prompt = prompt.replace(f"{{{{{key}}}}}", value)
    return prompt


def read_files(system_prompt_path, user_prompt_path, passage_path):

    with open(passage_path, "r", encoding='utf-8') as file:
        passage = file.read()
    
    with open(system_prompt_path, "r", encoding='utf-8') as file:
        system_prompt = file.read()
        
    user_prompt = replace_variable_in_prompt(user_prompt_path, {"passage": passage})
    
    return system_prompt, user_prompt, passage
    

if __name__ == "__main__":

    system_prompt_path = './prompts/system_prompt.txt'
    user_prompt_path = './prompts/user_prompt.txt'
    passage_path = './passages/haoyun.txt'
    system_prompt, user_prompt, passage = read_files(system_prompt_path, user_prompt_path, passage_path)
    
    # Generate a GED-style question
    question_string = generate_ged_style_question(system_prompt, user_prompt, passage)
    question_dict = get_structured_question(question_string)

    # Convert to JSON
    parsed_json = json.dumps(question_dict, indent=4)
    print(parsed_json)

    # print(question_string)