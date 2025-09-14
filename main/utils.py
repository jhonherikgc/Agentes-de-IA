from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# a variável 'docs' inciada antes de usá-la
docs = []

# Crie o 'splitter'
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)

# A linha abaixo vai procurar por todos os arquivos .pdf dentro da pasta "documents"
for n in Path("C:/Users/jhonherikgc/Documents/").glob("*.pdf"):
    try:
        loader = PyMuPDFLoader(str(n))
        docs.extend(loader.load())
        print(f"PDF carregado com sucesso {n.name}")
    except Exception as e:
        # Correção no formato da string: {n.name} e {e} separados
        print(f"Arquivo não encontrado {n.name}: {e}")

# Agora, a variável 'docs' já tem os dados e pode ser usada
chunks = splitter.split_documents(docs)

for chunk in chunks: 
    print(chunk)
    print("---------------------------------")

print (f"total de documentos carregados: {len(docs)}")
print (f"total de chunks criados: {len(chunks)}")