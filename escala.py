import pandas as pd
from datetime import datetime
import os

PLANILHA_ID = os.getenv("PLANILHA_ID")
SHEET_NAME = os.getenv("SHEET_NAME", "Escala")

import gspread
from oauth2client.service_account import ServiceAccountCredentials

def carregar_escala():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(PLANILHA_ID).worksheet(SHEET_NAME)
    data = sheet.get_all_records()
    return pd.DataFrame(data)

def buscar_plantao_por_atendente(nome, data=None):
    df = carregar_escala()
    nome = nome.lower()
    if data:
        data = datetime.strptime(data, "%Y-%m-%d").date()
        df = df[df["Data"] == data.strftime("%d/%m/%Y")]
    resultados = df[df["Atendente"].str.lower() == nome]
    return resultados.to_dict(orient="records")

def buscar_plantao_por_unidade(unidade, data=None):
    df = carregar_escala()
    unidade = unidade.lower()
    if data:
        data = datetime.strptime(data, "%Y-%m-%d").date()
        df = df[df["Data"] == data.strftime("%d/%m/%Y")]
    resultados = df[df["Unidade"].str.lower() == unidade]
    return resultados.to_dict(orient="records")