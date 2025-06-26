from mcp.tools import tool
from mcp.schema import ToolInput, ToolOutput
from pydantic import Field

class TesteInput(ToolInput):
    nome: str = Field(..., description="Nome da pessoa para dar oi")

class TesteOutput(ToolOutput):
    mensagem: str

@tool(name="hello_tool", input_model=TesteInput, output_model=TesteOutput)
def executar(input_data: TesteInput) -> TesteOutput:
    return TesteOutput(mensagem=f"Olá, {input_data.nome}! Bem-vindo ao MCP.")


