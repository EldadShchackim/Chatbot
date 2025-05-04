import requests
import gradio as gr

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
HEADERS = {"Authorization": "Bearer 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"}

def chat_with_bot(msg):
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": msg})
    result = response.json()
    return result[0]['generated_text']

chat_history = []

def chat_interface(user_input):
    response = chat_with_bot(user_input)
    chat_history.append(f"You: {user_input}")
    chat_history.append(f"Bot: {response}")
    with open('chat_log.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(chat_history))
    return response, "\n".join(chat_history)

css = """
    #chat-input textarea {
        background-color: #ffffff;
        color: #333;
        font-size: 16px;
        font-family: "Segoe UI", sans-serif;
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #ccc;
    }

    #chat-output textarea {
        background-color: #f0f9ff;
        color: #1a1a1a;
        font-size: 16px;
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #bbb;
        direction: rtl;
        text-align: right;
    }

    #submit-btn {
        background-color: #007BFF;
        color: white;
        font-size: 18px;
        padding: 12px 24px;
        border: none;
        border-radius: 30px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    #submit-btn:hover {
        background-color: #0056b3;
    }

    body .gradio-container {
        background-image: url("https://images.unsplash.com/photo-1503264116251-35a269479413");
        background-size: cover;
        background-position: center;
    }

    #chat-history textarea {
        background-color: #fffbea;
        color: #333;
        font-size: 14px;
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #aaa;
        height: 300px;
        overflow-y: scroll;
    }
"""

demo = gr.Interface(
    fn=chat_interface,
    inputs=gr.Textbox(label="Enter your message:", elem_id="chat-input"),
    outputs=[
        gr.Textbox(label="Bot's answer:", elem_id="chat-output"),
        gr.Textbox(label="Chat History:", elem_id="chat-history", lines=15)
    ],
    submit_btn = gr.Button("שלח", elem_id="submit-btn"),
    title=f"👋 ברוך הבא, אלדד",
    css=css
)

demo.launch(server_name="0.0.0.0", server_port=8080)
