from flask import request, jsonify
import os
import requests
from services.email_genai import EmailGenai
from services.extract_text import TextExtractor
from dotenv import load_dotenv
from auth.auth import connect_to_model_api


class AgentController:
    def __init__(self):
        pass

    @staticmethod
    def classify_and_respond(file_path):
        load_dotenv()
        try:
            text_extractor = TextExtractor(file_path)
            email_text = text_extractor.extract_text()

            api_url = connect_to_model_api()
            response = requests.post(api_url, json={"text": email_text})

            if response.status_code != 200:
                return {"error": "Erro ao chamar a API de classificação"}, 500

            result = response.json()
            prediction = result.get("prediction")
            class_name = result.get("class_name")

            if prediction == 0:
                classification = "improdutivo"
            elif prediction == 1:
                classification = "produtivo"
            else:
                classification = "desconhecido"

            system_instructions = f"""
            Você é um classificador de e-mails e seu papel é retornar uma resposta adequada para o e-mail, independente de ele ser produtivo ou não.

            O e-mail que você está respondendo é classificado como: {classification}

            Sua resposta deve ser sempre em JSON e seguir o seguinte formato:
            {{
                "response": "Sua resposta automatica aqui"
            }}
            """

            bot_response = EmailGenai.connect_agent(system_instructions, email_text)

            os.remove(file_path)  
            return {
                "bot_response": bot_response,
                "classification": classification,
                "api_response": result
            }, 200

        except Exception as e:
            return {"error": f"Erro no processo: {str(e)}"}, 500
