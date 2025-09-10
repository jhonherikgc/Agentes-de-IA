# importação do chat e requerimento da resposta do google gemini
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# carrega todas as variveis de ambiente do arquivo .env
load_dotenv()

# chama a api key da variavel de ambiente
GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY') 

# Se a chave da API não for encontrada no .env, exibe um erro e para a execução.
if not GOOGLE_API_KEY:
    print("Erro: A chave da API não foi encontrada. Verifique seu arquivo .env.")
    exit()

print("Chave de API carregada com sucesso.")

# configura o modelo de linguagem
# Passe a API key diretamente no parâmetro 'google_api_key'.
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", 
    temperature=0,
    google_api_key=GOOGLE_API_KEY,
)

# print da resposta
resp_test = llm.invoke("quem é você?")
print(resp_test.content)

TRIAGEM_PROMPT = (
    "Você é um professor de matemática / fisica que explica e tira dúvida dos usuários. "
    "Dada a mensagem do usuário, retorne SOMENTE um JSON com:\n"
    "{\n"
    '  "decisao": "AUTO_RESOLVER" | "PEDIR_INFO" | "EXPLICACAO_GERAL",\n'
    '  "dificuldade": "FACIL" | "MEDIO" | "DIFICIL",\n'
    '  "campos_faltantes": ["..."]\n'
    "}\n"
    "Regras:\n"
    '- **AUTO_RESOLVER**: Perguntas claras sobre matemática / fisica (Ex: "Qual é a raiz quadrada de 16?", "Quais são as leis de newton?").\n'
    '- **PEDIR_INFO**: Mensagens vagas ou que faltam informações para identificar o tema ou contexto (Ex: "Preciso de ajuda com funções", "Tenho uma dúvida geral").\n'
    '- **EXPLICACAO_GERAL**: Pedidos de exceção, ou quando o usuário explicitamente tem mais dúvidas recorrentes (Ex: "Não entendi, pode me explicar melhor?", "Como posso aplicar isso?", "Por favor me explique como se fosse uma criança").'
    "Analise a mensagem e decida a ação mais apropriada."
)