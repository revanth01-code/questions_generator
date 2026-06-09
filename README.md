# 🧠 Question Generator

An AI-powered question generator built with **Google Gemini** and **Gradio**, deployed on **Hugging Face Spaces**. Paste any study material or content and instantly generate MCQs, short-answer questions, or interview-style questions.

---

## 🚀 Demo

👉 [Live on Hugging Face Spaces](https://revanth-code-questions-generator.hf.space)

---

## ✨ Features

- **MCQs** – Multiple-choice questions for quick revision
- **Short Answer** – Concise questions for deeper understanding
- **Interview** – Professional interview-style questions from any content
- Powered by `gemini-2.5-flash-lite` for fast, quality output
- Simple and clean UI via Gradio

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| AI Model | Google Gemini 2.5 Flash Lite |
| SDK | `google-genai` |
| UI | Gradio |
| Deployment | Hugging Face Spaces |

---

## 📦 Installation (Run Locally)

**1. Clone the repository**

```bash
git clone https://github.com/revanth01-code/questions_generator.git
cd questions_generator
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Set up environment variables**

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

> Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

**4. Run the app**

```bash
python app.py
```

The app will be available at `http://localhost:7860`.

---

## 🤗 Deploying to Hugging Face Spaces

1. Create a new Space on [Hugging Face](https://huggingface.co/spaces) with the **Gradio** SDK.
2. Push your code to the Space repository.
3. Add your `GEMINI_API_KEY` as a **Secret** under *Settings → Repository Secrets*.

> Secrets are used instead of a `.env` file on Hugging Face Spaces.

---

## 📁 Project Structure

```
question-generator/
├── app.py               # Main application
├── requirements.txt     # Python dependencies
├── .env                 # API key (local only, do not commit)
└── README.md
```

---

## 📋 Requirements

```
google-genai
gradio
python-dotenv
```

---

## ⚠️ Notes

- Do **not** commit your `.env` file or expose your API key publicly.
- Add `.env` to your `.gitignore`.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
