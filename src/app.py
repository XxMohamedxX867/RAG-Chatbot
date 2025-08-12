from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
import uvicorn
import os
import tempfile
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
import json
from typing import Optional
import shutil
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="Luxury Hotel RAG Chatbot", version="1.0.0")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Global variables for RAG system
rag_chain = None
pdf_loaded = False

# Get API key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    print("Warning: GOOGLE_API_KEY environment variable not set!")

def initialize_rag_system():
    """Initialize the RAG system with the hotels details PDF"""
    global rag_chain, pdf_loaded
    
    if not GOOGLE_API_KEY:
        print("Cannot initialize RAG system: Google API key not configured")
        return False
    
    try:
        # Path to the hotels details PDF
        pdf_path = "data/hotels details.pdf"
        
        if not os.path.exists(pdf_path):
            print(f"PDF file not found: {pdf_path}")
            return False
        
        print(f"Loading PDF: {pdf_path}")
        
        # Load PDF
        loader = PyMuPDFLoader(pdf_path)
        docs = loader.load()
        texts = [doc.page_content for doc in docs]
        
        print(f"Loaded {len(texts)} pages from PDF")
        
        # Split text
        text_splitter = RecursiveCharacterTextSplitter(
            add_start_index=True,
            chunk_size=350,
            chunk_overlap=100,
            length_function=len
        )
        chunks = text_splitter.create_documents(texts)
        
        print(f"Created {len(chunks)} text chunks")
        
        # Embeddings
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=GOOGLE_API_KEY
        )
        
        # ChromaDB
        chroma_dir = tempfile.mkdtemp()
        db = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=chroma_dir,
            collection_name="hotel_chunks"
        )
        retriever = db.as_retriever()
        
        # LLM
        llm = ChatGoogleGenerativeAI(
            model="models/gemini-2.5-flash",
            google_api_key=GOOGLE_API_KEY
        )
        
        # Prompt for hotel context
        system_prompt = (
            "You are a helpful hotel concierge assistant. Use the given context to answer questions about the hotel. "
            "If you don't know the answer, say you don't know. "
            "Keep answers concise and friendly. Always be helpful and professional. "
            "Context: {context}"
        )
        prompt = ChatPromptTemplate.from_messages(
            [("system", system_prompt), ("human", "{input}")],
        )
        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        rag_chain = create_retrieval_chain(retriever, question_answer_chain)
        
        pdf_loaded = True
        print("RAG system initialized successfully!")
        return True
        
    except Exception as e:
        print(f"Error initializing RAG system: {str(e)}")
        return False

@app.on_event("startup")
async def startup_event():
    """Initialize RAG system when the server starts"""
    print("🏨 Starting Luxury Haven Hotel RAG Chatbot...")
    if initialize_rag_system():
        print("✅ RAG system ready - AI Concierge is available!")
    else:
        print("❌ RAG system failed to initialize")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the hotel landing page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(message: str = Form(...)):
    """Handle chat messages with RAG system"""
    global rag_chain
    
    if not rag_chain:
        return {"response": "AI Concierge is not available at the moment. Please try again later.", "status": "error"}
    
    try:
        result = rag_chain.invoke({"input": message})
        answer = result["answer"]
        return {"response": answer, "status": "success"}
    
    except Exception as e:
        return {"response": f"Error processing message: {str(e)}", "status": "error"}

@app.get("/api/status")
async def get_status():
    """Get the current status of the RAG system"""
    return {
        "pdf_loaded": pdf_loaded,
        "rag_ready": rag_chain is not None,
        "api_key_configured": bool(GOOGLE_API_KEY)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 