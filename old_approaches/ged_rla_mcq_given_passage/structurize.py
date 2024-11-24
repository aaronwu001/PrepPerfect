import json
import re

def get_structured_question(question_string):

    # Parsing the string
    parsed_data = {}

    # Extract question
    question_match = re.search(r'Question:\s*"(.*?)"', question_string, re.DOTALL)
    if question_match:
        parsed_data['question'] = question_match.group(1).strip()

    # Extract options
    options_match = re.findall(r'([A-D])\)\s*"(.*?)"', question_string, re.DOTALL)
    if options_match:
        parsed_data['options'] = {option: text.strip() for option, text in options_match}

    # Extract correct answer
    correct_answer_match = re.search(r'Correct Answer:\s*([A-D])\)\s*"(.*?)"', question_string, re.DOTALL)
    if correct_answer_match:
        parsed_data['correct_answer'] = {
            'option': correct_answer_match.group(1),
            'text': correct_answer_match.group(2).strip()
        }

    # Extract explanation
    explanation_match = re.search(r'Explanation:\s*(.*)', question_string, re.DOTALL)
    if explanation_match:
        parsed_data['explanation'] = explanation_match.group(1).strip()

    return parsed_data


if __name__ == '__main__':
    question_string = """
    Question: "Which quotation from the passage supports the idea that community involvement can lead to personal growth?"

    A) "Many individuals find joy in participating in various community activities."
    B) "Helping others often opens up opportunities for personal reflection."
    C) "Volunteering allows people to step out of their comfort zones and build new skills."
    D) "Community service is a vital part of a well-rounded education."

    Correct Answer: C) "Volunteering allows people to step out of their comfort zones and build new skills."

    Explanation: The correct answer, C, directly supports the idea that community involvement contributes to personal growth by highlighting how volunteering challenges individuals and helps them develop new abilities. Answer A, while related to joy in community activities, does not explicitly connect to personal growth. Answer B focuses on personal reflection rather than growth through actionable skills, and answer D discusses the educational aspect of community service without addressing personal development directly.
    """

    parsed_data = get_structured_question(question_string)

    # Convert to JSON
    parsed_json = json.dumps(parsed_data, indent=4)
    print(parsed_json)