from fastapi import FastAPI, Query
from escala import buscar_plantao_por_atendente, buscar_plantao_por_unidade
from typing import Optional

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://painel-roboplantoes-1.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"message": "API do Robô de Plantão funcionando"}

@app.get("/plantao/atendente")
def plantao_atendente(nome: str, data: Optional[str] = None):
    return buscar_plantao_por_atendente(nome, data)

@app.get("/plantao/unidade")
def plantao_unidade(unidade: str, data: Optional[str] = None):
    return buscar_plantao_por_unidade(unidade, data)
