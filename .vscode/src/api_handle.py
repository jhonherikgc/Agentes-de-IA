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
    model="gemini-2.0-flash",
    temperature=0,
    google_api_key=GOOGLE_API_KEY, 
)

# A partir daqui, seu código continua o mesmo
resp_test = llm.invoke("quem é você?")
print(resp_test.content)