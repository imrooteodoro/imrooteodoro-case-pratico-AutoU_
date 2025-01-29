import os
from dotenv import load_dotenv
from transformers import BertForSequenceClassification, BertTokenizer
from pathlib import Path


class NlpService:
    def __init__(self):
        load_dotenv()
        model_relative_path = os.getenv("MODEL_PATH")
        print(model_relative_path)
        self.model_full_path = Path(model_relative_path)

        if not self.model_full_path.exists():
            raise FileNotFoundError(f"O caminho do modelo não existe: {self.model_full_path}")

    def return_model(self):
        try:
            model = BertForSequenceClassification.from_pretrained(
                str(self.model_full_path),
                local_files_only=True
            )
            model.eval()
            return model
        except Exception as e:
            raise RuntimeError(f"Erro ao carregar o modelo: {e}")
    
    def return_tokenizer(self):
        try:
            tokenizer = BertTokenizer.from_pretrained(
                str(self.model_full_path),
                local_files_only=True
            )
            return tokenizer
        except Exception as e:
            raise RuntimeError(f"Erro ao carregar o tokenizador: {e}")
