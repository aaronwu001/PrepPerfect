import re

def get_question_json(question_string):
    """
    Parse the question string into a structured dictionary.
    """
    parsed_data = {}

    # Extract passage
    passage_match = re.search(r'Passage:\s*"(.+?)"', question_string, re.DOTALL)
    if passage_match:
        parsed_data['passage'] = passage_match.group(1).strip()

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
    explanation_match = re.search(r'Explanation:\s*(.*?)\n\nDistractor', question_string, re.DOTALL)
    if explanation_match:
        parsed_data['explanation'] = explanation_match.group(1).strip()

    # Extract distractor explanations
    distractor_explanations = {}
    distractors_match = re.findall(r'Distractor ([A-D]) is.*?:\s*(.*?)\.', question_string, re.DOTALL)
    for option, explanation in distractors_match:
        distractor_explanations[option] = explanation.strip()

    if distractor_explanations:
        parsed_data['distractors'] = distractor_explanations

    return parsed_data


if __name__ == "__main__":
    question_string = '''
    Passage: "Urban green spaces, such as parks and community gardens, play a vital role in enhancing city life. They not only provide residents with places to relax and socialize but also improve air quality and support biodiversity. With increasing urbanization, the presence of greenery helps mitigate the heat island effect caused by concrete and asphalt. Furthermore, these green areas can enhance property values, attract tourism, and decrease levels of stress for city dwellers. As cities evolve, incorporating more green spaces is essential for promoting sustainable urban development and fostering a healthier environment for all."

    Question: "What is the main idea of the passage?"

    A) "Urban green spaces benefit cities by increasing property values."
    B) "Community gardens are the most popular form of urban green space."
    C) "Green spaces help improve city life and contribute to environmental sustainability."
    D) "The heat island effect can be completely eliminated by planting more trees."

    Correct Answer: C) "Green spaces help improve city life and contribute to environmental sustainability."

    Explanation: The correct answer, C, captures the main idea of the passage, which emphasizes the multifaceted benefits of urban green spaces, including enhancing quality of life and supporting environmental wellbeing.

    Distractor A is partially accurate as it mentions increased property values, which is one of the benefits discussed, but it does not encompass the broader significance of green spaces as stated in the passage.

    Distractor B incorrectly limits the discussion to community gardens, failing to recognize that urban green spaces include a variety of forms, such as parks, and therefore does not represent the passage's main idea.

    Distractor D is misleading, as the passage discusses mitigating the heat island effect rather than eliminating it. This implies an unrealistic outcome and deviates from the overall theme of promoting urban greenery for numerous benefits.
    '''

    parsed_data = get_question_json(question_string)
    import json
    print(json.dumps(parsed_data, indent=4))
