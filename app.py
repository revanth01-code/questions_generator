from google import genai
from google.genai import types
import os 
from dotenv import load_dotenv
import gradio as gr

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

question_types = {
    "MCQs": "Generate multiple-choice questions from the given content.",
    "Short Answer": "Generate short-answer questions from the given content.",
    "Interview": "Generate interview-style questions from the given content."
}

def generate_questions(user_prompt,question_type):
    system_prompt = question_types.get(question_type, "Generate questions from the given content.")
    response = client.models.generate_content(
        model = "gemini-2.0-flash-lite",
        contents = user_prompt,
        config = types.GenerateContentConfig(
            system_prompt = system_prompt,
            temperature = 0.7,
            max_output_tokens = 500
        )
    )

    return response.text

demo = gr.Interface(
    fn = generate_questions,
    inputs=[
        gr.Textbox(
            lines=6,
            placeholder="Paste study material or content here...",
            label="Input Content"
        ),
        gr.Radio(
            choices=list(question_types.keys()),
            value="MCQs",
            label="Question Type"
        )
    ],
    outputs=gr.Textbox(lines=12, label="Generated Questions"),
    title="Question Generator",
    description="Generate MCQs, short-answer, or interview-style questions from given content using Gemini."
)

demo.launch(debug=True)
