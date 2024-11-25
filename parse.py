import json

def parse_questions_to_json(content):
    """
    Parses a string of questions into a JSON-compatible structure.

    Args:
        content (str): String containing questions formatted with specific delimiters.

    Returns:
        list: A list of dictionaries representing the parsed questions.
    """
    questions = []
    blocks = content.split('---')  # Split on separator "---"
    
    for block in blocks:
        question_data = {}
        lines = [line.strip() for line in block.split('\n') if line.strip()]
        for i, line in enumerate(lines):

            if line.startswith('- **Question Type:**'):
                question_data['Question Type'] = line.split(':', 1)[1].strip().lstrip('* ')

            elif line.startswith('- **Question:**'):
                question_data['Question'] = line.split(':', 1)[1].strip().lstrip('* ')

            elif line.startswith('- **Passage:**'):
                passage = line.split(':', 1)[1].strip().lstrip('* ')
                question_data['Passage'] = passage if passage != 'None' else None

            elif line.startswith('- **Options:**'):
                options = []
                for option_line in lines[i+1:]:
                    if not option_line.startswith('- '):
                        break
                    stripped_option_line = option_line.lstrip('- ')
                    if stripped_option_line.startswith('**'):
                        break
                    options.append(stripped_option_line)
                question_data['Options'] = options

            elif line.startswith('- **Correct Answer:**'):
                question_data['Correct Answer'] = line.split(':', 1)[1].strip().lstrip('* ')

            elif line.startswith('- **Explanation:**'):
                question_data['Explanation'] = line.split(':', 1)[1].strip().lstrip('* ')
            
        questions.append(question_data)

    return questions 


if __name__ == '__main__':
    # Define input and output file paths
    input_path = './output/questions_string.txt'
    output_path = './output/parsed_questions_testing.json'

    # Read the input file
    with open(input_path, 'r', encoding='utf-8') as file:
        questions_string = file.read()

    # Parse the questions string
    parsed_questions = parse_questions_to_json(questions_string)

    # Save the parsed output
    with open(output_path, 'w', encoding='utf-8') as output_file:
        json.dump(parsed_questions, output_file, indent=4, ensure_ascii=False)

    print(f"Parsed questions saved to: {output_path}")

