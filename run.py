#!/usr/bin/env python3
"""
Startup script for Luxury Haven Hotel RAG Chatbot
Run this file to start the FastAPI server
"""

import uvicorn
from src.app import app

if __name__ == "__main__":
    print("🏨 Starting Luxury Haven Hotel RAG Chatbot...")
    print("📍 Server will be available at: http://localhost:8000")
    print("📖 API documentation will be available at: http://localhost:8000/docs")
    print("🔄 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True,  # Enable auto-reload for development
        log_level="info"
    )
