# MCP Server Project

Este projeto inicia um servidor MCP local e integra com Azure OpenAI para realizar chamadas de ferramentas interativas.

## Requisitos

- Python 3.8+
- Node.js (para rodar o MCP)
- Azure OpenAI configurado
- Variáveis de ambiente no `.env`

## Como executar

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env .env  # e edite com seus dados
python src/main.py
```

