import os
from app.data_loader import load_ppt,split_text
from vectorstore.vectordb import create_vector_store
from models.groq_model_loader import load_llm
from langchain.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from app.prompt import SYSTEM_PROMPT

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# PPT_PATH = os.path.join(BASE_DIR, 'data/Employee_Leave_Policy.pptx')
PPT_PATH = ('D:/ChatBot/backend/data/Employee_Leave_Policy.pptx')

try:
    file_path = PPT_PATH
    documents = load_ppt(file_path)
    text_chunks = split_text(documents)
except Exception as e:
    print(f"Error loading or processing data: {e}")
    raise

try:
    vector_store = create_vector_store(text_chunks)
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})
except Exception as e:
    print(f"Error creating vector store: {e}")
    raise

try:
    llm = load_llm()
except Exception as e:
    print(f"Error loading LLM model: {e}")
    raise

try:
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ('human', "{input}")
    ])
except Exception as e:
    print(f"Error creating prompt template: {e}")
    raise


try:
    qanda_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, qanda_chain)
except Exception as e:
    print(f"Error creating chains: {e}")
    raise



def process_query(query: str) -> str:
    response = rag_chain.invoke({"input": query})
    return response['answer']
