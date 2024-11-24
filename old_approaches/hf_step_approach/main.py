import os
import dotenv
from hf_step_approach.article_summarize import summarize
from hf_step_approach.paraphrase import paraphrase

if __name__ == '__main__':
    # Obtain Huggingface Access Token
    dotenv.load_dotenv()
    HF_TOKEN = os.getenv('HF_TOKEN')

    # Read the article from the file
    file_path = "sample_article.txt"  # Replace with your file path
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        exit()

    # identify key sentences/concepts
    summary = summarize(text, HF_TOKEN)

    # paraphrase the key sentences/conepts
    p = paraphrase(summary, HF_TOKEN)
    print('========')
    print(p)
    print('========')

    
        
