# main.py
#bibliotecas matemáticas
import sympy as sp
import numpy as np

#bibliotecas usadas para a triagem
from pydantic import BaseModel, Field
from typing import Literal, List, Dict
from langchain_core.messages import SystemMessage, HumanMessage

# Importa a instância 'llm' e a variável 'GOOGLE_API_KEY' do seu api_handler.
# Se você tiver um arquivo api_handler, é de lá que você deve importar
from api_handle import llm

# ---
# Aqui está o seu prompt
TRIAGEM_PROMPT = (
    "Você é um professor de matemática / fisica que explica e tira dúvida dos usuários. "
    "Dada a mensagem do usuário, retorne SOMENTE um JSON com:\n"
    "{\n"
    '   "decisao": "AUTO_RESOLVER" | "PEDIR_INFO" | "EXPLICACAO_GERAL",\n'
    '   "dificuldade": "FACIL" | "MEDIO" | "DIFICIL",\n'
    '   "campos_faltantes": ["..."]\n'
    "}\n"
    "Regras:\n"
    '- **AUTO_RESOLVER**: Perguntas claras sobre matemática / fisica (Ex: "Qual é a raiz quadrada de 16?", "Quais são as leis de newton?").\n'
    '- **PEDIR_INFO**: Mensagens vagas ou que faltam informações para identificar o tema ou contexto (Ex: "Preciso de ajuda com funções", "Tenho uma dúvida geral").\n'
    '- **EXPLICACAO_GERAL**: Pedidos de exceção, ou quando o usuário explicitamente tem mais dúvidas recorrentes (Ex: "Não entendi, pode me explicar melhor?", "Como posso aplicar isso?", "Por favor me explique como se fosse uma criança").'
    "Analise a mensagem e decida a ação mais apropriada."
)
# ---

# classe resposavel pela avaliação da triagem do prompt
class TriagemOut(BaseModel):
    decisao: Literal["AUTO_RESOLVER", "PEDIR_INFO", "EXPLICACAO_GERAL"]
    dificuldade: Literal["FACIL", "MEDIO", "DIFICIL"]
    campos_faltantes: List[str] = Field(default_factory=list)

# llm_triagem já está definida no api_handler, não precisa ser criada aqui novamente.
triagem_chain = llm.with_structured_output(TriagemOut)

def triagem (mensagem: str) -> Dict:
    saida: TriagemOut = triagem_chain.invoke([
        SystemMessage(content=TRIAGEM_PROMPT), 
        HumanMessage(content=mensagem)
    ])
    return saida.model_dump()

teste = ["Qual é a raiz quadrada de 16?",
    "Me explique funções matematicas.",
    "Como funciona algebra Linear?",
    "Quais são todos os ramos da matemática?"]

for msg_teste in teste:
    print(f"Pergunta: {msg_teste}\n -> Resposta: {triagem(msg_teste)}\n ")