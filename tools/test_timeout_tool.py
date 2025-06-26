import asyncio
from mcp.schema import ToolInput, ToolOutput
from mcp.tools import tool

class TimeoutInput(ToolInput):
    duration_seconds: int = 1800  # até 30 minutos

class TimeoutOutput(ToolOutput):
    message: str

@tool(name="simular_execucao_longa", description="Tool que executa por muito tempo para testar timeout")
async def simular_execucao_longa(input: TimeoutInput) -> TimeoutOutput:
    max_duration = 1800  # 30 minutos

    duration = min(input.duration_seconds, max_duration)

    print(f"Iniciando execução longa por {duration} segundos...")

    # Loop com pequenos sleeps para simular atividade contínua
    for i in range(duration):
        await asyncio.sleep(1)
        if i % 60 == 0:
            print(f"{i//60} minutos passados...")

    return TimeoutOutput(message=f"Execução finalizada após {duration} segundos.")
