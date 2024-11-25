# PrepEmpower: GED RLA Question Generation

## Overview

This project processes a PDF containing GED RLA multiple-choice questions and generates new GED-style questions in a structured JSON format, suitable for frontend integration. The system leverages OpenAI's GPT models for question generation with rigorous formatting and diverse question types.

## Features

- **PDF Processing:** Extracts text from GED RLA PDF documents.
- **AI-Powered Generation:** Utilizes OpenAI's GPT models for question creation.
- **Custom Parsing:** Outputs JSON-formatted questions for easy integration.
- **Scalable Design:** Focused on GED RLA but adaptable to other domains.

---

## How to Run

1. **Install Dependencies: Make sure Python 3.x is installed. Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Set OpenAI API Key:**

   - Copy .env.example to .env

   ```bash
   cp .env.example .env
   ```

   - Add your OpenAI API key to the .env file:

   ```bash
   OPENAI_API_KEY=your-api-key
   ```

3. **Run The Main Script**

   - Place your GED RLA PDF file in the materials/ folder.

   ```bash
   python mcq_from_sample.py
   ```

4. **View The Output**
   - Generated questions will be saved in the output/ folder as:
     questions_string.txt (raw questions)
     parsed_questions.json (structured JSON)

## Folder Structure

```
project/
├── materials/          # Input PDFs and related content
├── old_approaches/     # Previous methodologies
├── output/             # Generated questions and JSON outputs
├── mcq_from_sample.py  # Main script for question generation
├── parse.py            # Parsing script for structured JSON
└── .env.example        # Environment variable example file
```

## Approaches

1. **Initial Attempts:**
   - Explored Hugging Face models but faced input size limitations and complexity.
   - Attempted chunking articles, extracting keywords, and generating questions with distractors.
   - Abandoned due to inefficiencies.
2. **Passage-Based Questions:**
   - Generated questions from single passages but required manual passage collection.
3. **Free Generation:**
   - Prompted for random questions but suffered from topic repetition and limited diversity in question types.
4. **Current Approach:**
   - Reads GED RLA guides, extracts question patterns, and generates diverse questions with balanced formats.

## Challenges

- **Consistency:** Ensuring JSON output is rigorous and reliable.
- **Repetition Avoidance:** Managing diverse topics and question types without manual intervention.
- **Prompt Engineering:** Fine-tuning prompts for clear instructions and consistent outputs.

## Dependencies

- Python 3.x
- Required packages: openai, python-dotenv, pdfplumber
  Install dependencies with:
  `bash
pip install -r requirements.txt
`

## Future Enhancements

- Automate topic and type tracking for balanced question generation.
- Extend functionality to other exam formats and subjects.
- Randomize topic selection while avoiding repetitions.

## Further Context

### Key Insights from Old Approaches

1. Hugging Face APIs:

   - Initially used Hugging Face APIs but found no suitable models that could handle large GED RLA-style input scripts.
   - Experimented with chunking, keyword extraction, and creating distractors, but this was time-consuming and inefficient.

2. Passage Collection:

   - Tried generating a single question (e.g., about the main idea) for each passage. This worked but required continuous collection of new passages, which was impractical.

3. Free Generation:
   - Attempted free generation by instructing the model to create GED RLA-style MCQs. This approach had issues with:
     - Repetition of topics mentioned in the prompt.
     - Limited diversity, focusing mostly on "main idea" questions.

### Current Approach

The current solution reads sample questions from the official GED RLA guide. By analyzing patterns and question types in the guide, the system generates consistent and diverse questions with a balance between passage-based and non-passage-based types. This approach ensures high-quality output while minimizing manual effort.

## 🤝 Contribution to Rutgers Enactus

This project is part of the **New Beginnings Project** for **Rutgers Enactus**, an initiative focused on supporting rehabilitated individuals as they reintegrate into society. By providing **personalized educational tools**, we aim to empower individuals to achieve their **GED certification** and gain the skills needed for brighter futures.

The ultimate vision of this project is to expand beyond GED preparation, offering modules in practical areas such as **personal finance** and **basic law**, ensuring rehabilitated individuals are equipped with the knowledge they need to succeed.
