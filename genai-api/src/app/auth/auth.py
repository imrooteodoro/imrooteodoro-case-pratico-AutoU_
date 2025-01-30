import os
from dotenv import load_dotenv


def authenticate_with_genai():
    load_dotenv()
    keypass = os.getenv('api_key')
    return keypass

def connect_to_model_api():
    load_dotenv()
    apiUrl = os.getenv('api_url')
    return apiUrl