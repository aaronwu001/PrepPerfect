import requests
import re

def split_article(text, max_chunk_size=1024, overlap=1):
    """
    Split the text into chunks of up to max_chunk_size characters, respecting sentence boundaries.
    Ensure overlap by including the last 'overlap' sentences of the previous chunk in the next chunk.
    """
    chunks = []
    for i in range(0, len(text) - 1024 * 2, 1024):
        chunks.append(text[i:i+3072])
    return chunks


    # chunks = []
    # start_idx = 0

    # while start_idx < len(text):
    #     # Define a window for splitting
    #     window = text[start_idx:start_idx + max_chunk_size]

    #     # Find the last sentence-ending punctuation within the window
    #     pattern = r"[.!?]\s?"
    #     matches = list(re.finditer(pattern, window))
    #     if matches:
    #         # End at the last punctuation within the window
    #         end_idx = matches[-1].end() + start_idx
    #     else:
    #         # If no punctuation, take the full window
    #         end_idx = start_idx + max_chunk_size

    #     # Create a chunk and append
    #     chunk = text[start_idx:end_idx].strip()
    #     chunks.append(chunk)

    #     # Overlap: Include the last 'overlap' sentences in the next chunk
    #     overlap_pattern = r"(.*?[.!?])"
    #     overlap_matches = list(re.finditer(overlap_pattern, chunk))
    #     if overlap and overlap_matches:
    #         overlap_text = " ".join([m.group(0) for m in overlap_matches[-overlap:]])
    #     else:
    #         overlap_text = ""

    #     # Move the start index forward, keeping the overlap
    #     start_idx = end_idx - len(overlap_text)

    # return chunks



def summarize(text, HF_TOKEN):
    # split the article into chunks
    chunks = split_article(text)
    
    # summarize each chunk 
    summaries = []
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

    for chunk in chunks:
        
        payload = {
            "inputs": chunk,
            "parameters": {
                "max_length": 150,
                "min_length": 30
            }
        }
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code}, {response.text}")
        
        summary = response.json()[0]['summary_text']
        summaries.append(summary)
        print(summary)
        print('==========================')

    return "\n".join(summaries)
        