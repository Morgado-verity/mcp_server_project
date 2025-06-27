import os
import requests
from fastmcp import tool

# Obtém a chave da API a partir das variáveis de ambiente.
# Lembre-se de criar um ficheiro .env na raiz do seu projeto e adicionar:
# OPENWEATHER_KEY="sua_chave_aqui"
OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")

# --- Definição dos Modelos de Entrada e Saída ---

# --- Definição da Ferramenta ---
# 3. Decorador @tool atualizado:
#    Os dois primeiros argumentos são agora, obrigatoriamente, as classes
#    de Input e Output que acabámos de definir.
@tool()
def clima_hoje(input: str) -> str:
    """
      Retorna a previsão atual do tempo na cidade informada (ex: Rio de Janeiro), incluindo a descrição do clima e temperatura em Celsius.
    Args:
        input: Uma instância de ClimaInput, contendo o campo 'cidade'.

    Returns:
        Uma instância de ClimaOutput, contendo o campo 'clima_info'.
    """
    if not OPENWEATHER_KEY:
        # 4. Retorno em caso de erro: Sempre retorna uma instância da classe de Output.
        return "Erro: A chave da API OpenWeatherMap (OPENWEATHER_KEY) não foi configurada."

    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": input.cidade, # Acede ao parâmetro através de input.cidade
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
        
        # 5. Retorno em caso de sucesso: Também retorna uma instância da classe de Output.
        return f"O clima em {input.cidade} é '{clima}' com temperatura de {temp}°C."
    
    except Exception as e:
        return f"Erro inesperado ao buscar clima: {str(e)}"
