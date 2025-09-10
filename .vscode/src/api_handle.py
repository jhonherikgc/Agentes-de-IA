import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY') 

if not GOOGLE_API_KEY:
    print("Erro: A chave da API não foi encontrada. Verifique seu arquivo .env.")
    exit()

print(f"Sua chave foi encontrada! \n Chave da API: {GOOGLE_API_KEY[:4]}...{GOOGLE_API_KEY[-4:]} foi carregada com sucesso.")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", 
    temperature=0,
    google_api_key=GOOGLE_API_KEY,
)