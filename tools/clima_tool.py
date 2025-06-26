from mcp.tools import tool
import requests
import os

OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")

@tool
def clima_hoje(cidade: str) -> str:
    """
    Retorna a previsão atual do tempo na cidade informada (ex: Rio de Janeiro),
    incluindo a descrição do clima e temperatura em Celsius. Ideal para perguntas como
    'como está o clima hoje em São Paulo?' ou 'qual a temperatura agora no Rio?'.
    """
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": cidade,
            "appid": OPENWEATHER_KEY,
            "lang": "pt_br",
            "units": "metric"
        }
        response = requests.get(url, params=params)
        dados = response.json()

        if response.status_code != 200:
            return f"Erro: {dados.get('message', 'Cidade não encontrada')}"

        clima = dados["weather"][0]["description"]
        temp = dados["main"]["temp"]
        return f"O clima em {cidade} é '{clima}' com temperatura de {temp}°C."
    except Exception as e:
        return f"Erro ao buscar clima: {str(e)}"
