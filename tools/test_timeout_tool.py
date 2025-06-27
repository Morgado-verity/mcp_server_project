# tools/test_timeout_tool.py
import asyncio
# 1. Importe as classes e o decorador diretamente de 'fastmcp'.
from fastmcp import tool

# 3. Use o decorador @tool com a assinatura correta.
#    Os dois primeiros argumentos são as classes de Input e Output.
#    O 'name' é opcional (pode ser inferido do nome da função), mas é bom ser explícito.
@tool()
def simular_execucao_longa(input: int) -> str:
    # 4. A descrição para a IA está aqui, na docstring da função.
    """
    Ferramenta que executa por um determinado número de segundos. 
    Útil para testar comportamentos de longa duração e timeouts.
    """
    max_duration = 1800  # Limite máximo de 30 minutos por segurança
    
    # Acede ao valor de entrada através do objeto 'input'.
    duration = min(input.duration_seconds, max_duration)
    
    print(f"Iniciando execução longa por {duration} segundos...")
    
    # Esta função é síncrona, então usamos time.sleep.
    # Se fosse 'async def', usaríamos 'await asyncio.sleep()'.
    for i in range(duration):
        # A lógica da sua ferramenta vai aqui.
        # time.sleep(1) # Removido para testes mais rápidos
        pass
    
    print("Execução longa finalizada.")
            
    # 5. Retorne uma instância da sua classe de Output.
    return f"Execução finalizada após {duration} segundos."
