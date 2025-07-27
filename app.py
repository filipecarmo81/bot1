from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()

# Recupera a chave da API da OpenAI da variável de ambiente
openai.api_key = os.environ.get("OPENAI_API_KEY")

class Pergunta(BaseModel):
    texto: str

@app.post("/perguntar")
def perguntar(p: Pergunta):
    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um assistente de atendimento com base em um manual do paciente."},
            {"role": "user", "content": p.texto}
        ]
    )
    return {"resposta": resposta['choices'][0]['message']['content']}
