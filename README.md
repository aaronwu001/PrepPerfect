# PrepEmpower: AI-Powered Practice Test Platform for GED Preparation

PrepEmpower is an AI-driven practice test platform designed to help rehabilitated individuals prepare for their **GED (General Educational Development)** certification. This project is part of my contribution to the **New Beginnings Project** for **Rutgers Enactus**, which aims to support individuals in their journey toward reintegration into society through education and skill development.

The platform focuses on creating dynamic and personalized practice tests using **OpenAI's API**, starting with **GED Reading and Language Arts (RLA)**. It is designed to make GED preparation accessible and effective while leveraging the power of artificial intelligence.

---

## 🚀 Project Vision

### Why PrepEmpower?
- **Empowering Education**: Provide rehabilitated individuals with the tools they need to achieve their GED certification.
- **AI-Powered Learning**: Harness the power of AI to generate engaging, high-quality practice questions.
- **Scalable Impact**: Expand the system to other GED courses and practical topics, such as **personal finance** and **basic law**, to support a broader range of educational needs.

### Goals:
1. **GED Practice Tests**:
   - Build personalized practice tests for all GED subjects, starting with RLA.
2. **Expand Educational Modules**:
   - Develop content for personal finance, basic law, and other practical life skills.
3. **Rehabilitation Through Education**:
   - Create accessible tools that empower individuals for brighter futures.

---

## 📋 Current Status

### Progress So Far:
- **Completed**:
  - **RLA Module (In Progress)**:
    - Developed one question type: **"Which quotation from the passage supports a given idea?"**
    - Dynamically generates questions using OpenAI's GPT-4 API.
- **Work in Progress**:
  - Expanding to additional question types (e.g., inference, vocabulary-in-context).
  - Exploring scalable approaches for other GED courses.

### Future Goals:
1. **Complete RLA Question Types**:
   - Add support for inference, main idea identification, and other critical question types.
2. **Expand to Other GED Subjects**:
   - Start creating practice tests for Math, Science, and Social Studies.
3. **Develop Practical Modules**:
   - Build modules for personal finance and legal basics to support life skills education.
4. **Mock Test Integration**:
   - Combine generated questions into full-length mock GED tests.

---

## 🛠️ How to Use (updated Nov. 18th 2024)

### 1. Prepare Inputs
- Place the passage you want to use for question generation in the `passages/` directory (e.g., `passage1.txt`).
- Define the prompts for AI in the `prompts/` directory:
  - `system_prompt.txt`: Provides the context and role for the AI assistant.
  - `user_prompt.txt`: Defines the task and formatting for the questions.

### 2. Add Your OpenAI API Key
Create a `.env` file in the root directory and add your OpenAI API key:
```plaintext
OPENAI_API_KEY=your_openai_api_key
```

### 3. Run the Program 
Execute the main script using:
```bash
python main.py
```

### 4. Review the Output
The program will generate a GED-style question based on the provided passage and prompts. Example output:
```plaintext
Generated Question:
Which quotation from the passage supports the idea that the fight was not well-received by critics?

A) "Quotation A"
B) "Quotation B"
C) "Quotation C"
D) "Quotation D"

Correct Answer: C) "Quotation C"
Explanation: This quote directly addresses the critics' sentiment, making it the best choice.
```

## 🌟 Key Features

1. **Dynamic Placeholder Replacement**:
   - Uses `{{text}}` variables in the prompts, dynamically replaced with passage content for flexibility and reusability.

2. **AI-Powered Question Generation**:
   - Generates high-quality, multiple-choice GED questions tailored to the input passage using OpenAI's API.

3. **Scalability**:
   - Easily extendable to other GED subjects (Math, Science, and Social Studies) and additional question types.

4. **Practice-Focused**:
   - Designed to provide targeted practice for rehabilitated individuals working toward GED certification.

5. **Educational Impact**:
   - Supports the development of essential skills, empowering individuals with practical and actionable learning tools.

---

## 📈 Project Updates

### Current Progress:
- **Completed**:
  - Implemented question generation for one type of GED RLA question: **"Which quotation from the passage supports a given idea?"** using OpenAI's API.
- **In Progress**:
  - Expanding to additional question types for RLA, such as inference and vocabulary-based questions.

### Upcoming Goals:
1. **Additional Question Types**:
   - Develop and integrate more question types for GED Reading and Language Arts.
2. **Extend to Other GED Subjects**:
   - Begin developing practice tests for Math, Science, and Social Studies.
3. **Mock Exam Integration**:
   - Combine generated questions into full-length practice tests for a comprehensive preparation experience.
4. **User Feedback and Testing**:
   - Pilot the system with rehabilitated individuals to refine and improve the educational modules.

---

## 🤝 Contribution to Rutgers Enactus

This project is part of the **New Beginnings Project** for **Rutgers Enactus**, an initiative focused on supporting rehabilitated individuals as they reintegrate into society. By providing **personalized educational tools**, we aim to empower individuals to achieve their **GED certification** and gain the skills needed for brighter futures.

The ultimate vision of this project is to expand beyond GED preparation, offering modules in practical areas such as **personal finance** and **basic law**, ensuring rehabilitated individuals are equipped with the knowledge they need to succeed.

---

## 📝 License

This project is licensed under the MIT License. See `LICEN


