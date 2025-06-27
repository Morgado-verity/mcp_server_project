# src/test_client_stdio.py
import asyncio
import logging

# 1. Importa o StdioClient, específico para este tipo de transporte.
from fastmcp import StdioClient

# Configura o logging para ver menos mensagens durante o teste.
logging.basicConfig(level=logging.WARNING)

async def test_server():
    """
    Este script atua como um cliente MCP para testar o servidor localmente,
    iniciando-o como um subprocesso e comunicando-se via stdio.
    """
    print("--- Iniciando cliente de teste para o servidor MCP via stdio ---")

    # 2. Define o comando para iniciar o seu servidor.
    #    Este comando será executado como um subprocesso pelo cliente.
    server_command = ["python", "-m", "src.main"]

    # 3. Conexão com o Servidor via stdio
    #    O StdioClient gere o ciclo de vida do processo do servidor.
    async with StdioClient(server_command) as client:
        print(">>> Sessão MCP estabelecida com sucesso via stdio.")

        # O restante da lógica de teste é exatamente a mesma!
        # A abstração do 'client' cuida da diferença de transporte.

        # 4. Teste 1: Listar as ferramentas disponíveis.
        print("\n--- Testando 'list_tools' ---")
        tools = await client.list_tools()
        tool_names = [tool.name for tool in tools]
        print(f"Ferramentas encontradas: {tool_names}")
        assert "clima_hoje" in tool_names
        assert "simular_execucao_longa" in tool_names
        print(">>> Teste de list_tools: SUCESSO")

        # 5. Teste 2: Chamar a ferramenta 'clima_hoje'.
        print("\n--- Testando 'call_tool' com 'clima_hoje' ---")
        cidade = "São Paulo"
        args = {"cidade": cidade}
        print(f"Chamando 'clima_hoje' com argumentos: {args}")
        result = await client.call_tool("clima_hoje", args)
        print(f"Resultado recebido: {result}")
        assert "°C" in result
        print(">>> Teste de clima_hoje: SUCESSO")

        # 6. Teste 3: Chamar a ferramenta 'simular_execucao_longa'.
        print("\n--- Testando 'call_tool' com 'simular_execucao_longa' ---")
        duration = 2
        args_timeout = {"duration_seconds": duration}
        print(f"Chamando 'simular_execucao_longa' com argumentos: {args_timeout}")
        result_timeout = await client.call_tool("simular_execucao_longa", args_timeout)
        print(f"Resultado recebido: {result_timeout}")
        assert f"{duration} segundos" in result_timeout
        print(">>> Teste de simular_execucao_longa: SUCESSO")

        print("\n--- Todos os testes foram concluídos com sucesso! ---")


if __name__ == "__main__":
    try:
        asyncio.run(test_server())
    except Exception as e:
        print(f"\nERRO: Ocorreu um problema ao executar o servidor.")
        print(f"Detalhe do erro: {e}")
