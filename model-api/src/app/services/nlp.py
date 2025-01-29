import os
from dotenv import load_dotenv
from transformers import BertForSequenceClassification, BertTokenizer

class NlpService:
    def __init__(self):
        load_dotenv()
        model_name = os.getenv("MODEL_PATH") 
        
        if not model_name:
            raise ValueError("MODEL_PATH não encontrado no arquivo .env")
        
        self.model_name = model_name

    def return_model(self):
        try:
            model = BertForSequenceClassification.from_pretrained(self.model_name)
            model.eval()
            return model
        except Exception as e:
            raise RuntimeError(f"Erro ao carregar o modelo: {e}")
    
    def return_tokenizer(self):
        try:
            tokenizer = BertTokenizer.from_pretrained(self.model_name)
            return tokenizer
        except Exception as e:
            raise RuntimeError(f"Erro ao carregar o tokenizador: {e}")
