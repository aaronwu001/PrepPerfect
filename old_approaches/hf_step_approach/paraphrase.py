import requests

def paraphrase_t5_api(text, HF_TOKEN, model_name="t5-base"):
    """
    Paraphrase text using the Hugging Face API with the T5 model.
    
    :param text: The input text to be paraphrased.
    :param HF_TOKEN: Your Hugging Face API token.
    :param model_name: The model to use for paraphrasing (default: "t5-base").
    :return: The paraphrased text.
    """
    # Define the API URL for the chosen model
    API_URL = f"https://api-inference.huggingface.co/models/{model_name}"

    # Headers for authorization
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}

    # Add the "paraphrase:" prefix to instruct the model
    payload = {
        "inputs": f"paraphrase: {text}",
        "parameters": {
            "max_length": 512,
            "temperature": 0.8,  # Add randomness for more variation
            "top_p": 0.9        # Use nucleus sampling
        }
    }

    # Make the POST request to the API
    response = requests.post(API_URL, headers=headers, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            # Extract the paraphrased text
            result = response.json()
            if isinstance(result, list):
                return result
            else:
                raise ValueError("Unexpected response format from API.")
        except Exception as e:
            raise Exception(f"Error parsing API response: {e}")
    else:
        raise Exception(f"API Error: {response.status_code} - {response.text}")


# Example usage
import os
import dotenv
if __name__ == "__main__":
    dotenv.load_dotenv()
    HF_TOKEN = os.getenv('HF_TOKEN')

    # Input text to be paraphrased
    input_text = """
    Jake Paul beat Mike Tyson by unanimous decision in Dallas on Friday night.
    The former Youtuber had not fought professionally for almost 20 years.
    A record 60 million households tuned in to watch the fight on Netflix.
    """

    try:
        # Call the paraphrase function
        paraphrased_output = paraphrase_t5_api(input_text, HF_TOKEN)
        print("Paraphrased Text:")
        print(paraphrased_output)
    except Exception as e:
        print(f"Error: {e}")
