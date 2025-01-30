import google.generativeai as genai
from auth.auth import authenticate_with_genai


class EmailGenai:
    def __init__(self):
        pass

    def connect_agent(system_intructions, email_body):
        genai.configure(api_key = authenticate_with_genai())
        generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 20,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction=f"{system_intructions}",
        )

        chat_session = model.start_chat(
        history=[
        ]
        )

        response = chat_session.send_message(f"{email_body}")

        return response.text