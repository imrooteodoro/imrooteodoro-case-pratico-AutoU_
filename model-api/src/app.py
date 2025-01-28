import os
import sys
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
from services.nlp import NlpService 


sys.path.append(os.path.dirname(os.path.abspath(__file__)))


app = FastAPI()

nlp_service = NlpService()
model = nlp_service.return_model()
tokenizer = nlp_service.return_tokenizer()

class TextInput(BaseModel):
    text: str

@app.post("/predict/")
async def predict(input_data: TextInput):
    try:
        inputs = tokenizer(
            input_data.text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=512
        )
        
        with torch.no_grad():
            outputs = model(**inputs)
            prediction = torch.argmax(outputs.logits, dim=-1).item()
        
        return {
            "prediction": prediction,
            "class_name": model.config.id2label.get(prediction, "desconhecido")
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro na predição: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
