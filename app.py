from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()

# Chave da API da OpenAI (ideal usar variável de ambiente depois)
openai.api_key = "SUA_CHAVE_OPENAI"

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
