import os
import requests
from fastmcp import FastMCP
from pydantic import BaseModel

mcp = FastMCP(name="MainServer")

OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")

# Define os modelos de Input e Output para a ferramenta de clima.
class ClimaInput(BaseModel):
    cidade: str

class ClimaOutput(BaseModel):
    clima_info: str

@mcp.tool()
def clima_hoje(input: ClimaInput) -> ClimaOutput:
    """
    Retorna a previsão atual do tempo na cidade informada, incluindo a 
    descrição do clima e temperatura em Celsius.
    """
    if not OPENWEATHER_KEY:
        return ClimaOutput(clima_info="Erro: Chave da API OPENWEATHER_KEY não configurada.")

    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"q": input.cidade, "appid": OPENWEATHER_KEY, "lang": "pt_br", "units": "metric"}
        response = requests.get(url, params=params)
        response.raise_for_status()
        dados = response.json()

        clima = dados["weather"][0]["description"]
        temp = dados["main"]["temp"]
        
        return ClimaOutput(clima_info=f"O clima em {input.cidade} é '{clima}' com temperatura de {temp}°C.")
    
    except requests.exceptions.HTTPError as http_err:
        return ClimaOutput(clima_info=f"Erro de API: {http_err.response.json().get('message', 'Cidade não encontrada')}")
    except Exception as e:
        return ClimaOutput(clima_info=f"Erro inesperado: {str(e)}")

# Define os modelos de Input e Output para a ferramenta de timeout.
class TimeoutInput(BaseModel):
    duration_seconds: int

class TimeoutOutput(BaseModel):
    message: str

@mcp.tool()
async def simular_execucao_longa(input: TimeoutInput) -> TimeoutOutput:
    """
    Executa uma tarefa por um determinado número de segundos para 
    testar comportamentos de longa duração.
    """
    max_duration = 1800 
    duration = min(input.duration_seconds, max_duration)
    
    print(f"Iniciando execução longa por {duration} segundos...")
    
    await asyncio.sleep(duration)
            
    return TimeoutOutput(message=f"Execução finalizada após {duration} segundos.")


if __name__ == "__main__":
    import asyncio
    print("Iniciando servidor MCP na porta 8000...")
    asyncio.run(
        mcp.run_sse_async(
            host="127.0.0.1",
            port=8000,
            log_level="debug"
        )
    ) 