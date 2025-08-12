# 🏨 Luxury Haven Hotel - AI Concierge Chatbot

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-0.1+-orange.svg)](https://langchain.com/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-AI-red.svg)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A beautiful hotel landing page with an integrated AI-powered concierge chatbot using FastAPI and RAG (Retrieval-Augmented Generation) technology. The system automatically loads hotel information from a PDF document and provides instant, intelligent responses to guest inquiries.

## ✨ Features

- 🎨 **Modern Hotel Landing Page**: Beautiful, responsive design with luxury aesthetics
- 🤖 **AI Concierge Chatbot**: Powered by Google's Gemini AI and RAG technology
- 📄 **Automatic PDF Processing**: Pre-loaded hotel information from `data/hotels details.pdf`
- 🔍 **Smart Information Retrieval**: Get instant, accurate answers based on hotel content
- 📱 **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- ⚡ **FastAPI Backend**: High-performance Python backend with async support
- 🔐 **Secure API Management**: Environment variable-based configuration
- 🎯 **Floating Chat Interface**: Easy-to-access chatbot icon that opens on click

## 🚀 Live Demo

- **Website**: [http://localhost:8000](http://localhost:8000)
- **API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Interactive API Docs**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🛠️ Technology Stack

- **Backend**: FastAPI, Python 3.8+
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **AI/ML**: LangChain, Google Gemini AI, ChromaDB
- **Document Processing**: PyMuPDF
- **Styling**: Custom CSS with Font Awesome icons
- **Environment**: python-dotenv

## 📋 Prerequisites

- Python 3.8 or higher
- Google AI API key (for Gemini AI)
- PDF document containing hotel information

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/luxury-haven-hotel-chatbot.git
cd luxury-haven-hotel-chatbot
```

### 2. Set Up Environment

Create a `.env` file in the root directory:

```bash
# Copy the example file
cp .env.example .env

# Edit the .env file and add your Google API key
GOOGLE_API_KEY=your_actual_api_key_here
```

**Get your Google AI API key from**: [Google AI Studio](https://makersuite.google.com/app/apikey)

### 3. Install Dependencies

```bash
# Create and activate virtual environment
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Run the Application

```bash
# Start the FastAPI server
python -m uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload
```

### 5. Access the Website

Open your browser and go to: [http://localhost:8000](http://localhost:8000)

## 🎯 How It Works

### System Architecture

1. **PDF Loading**: On startup, the system automatically loads `data/hotels details.pdf`
2. **Text Processing**: PDF content is split into manageable chunks
3. **Vector Embeddings**: Text chunks are converted to embeddings using Google's AI
4. **Vector Database**: Embeddings are stored in ChromaDB for fast retrieval
5. **RAG Chain**: LangChain creates a retrieval-augmented generation pipeline
6. **AI Responses**: Gemini AI generates contextual answers based on retrieved information

### User Experience

1. **Visit Website**: Beautiful hotel landing page loads
2. **Click Chat Icon**: Floating chat icon in bottom-right corner
3. **Start Chatting**: AI Concierge is immediately ready to help
4. **Get Answers**: Intelligent responses based on hotel information

## 📁 Project Structure

```
luxury-haven-hotel-chatbot/
├── src/
│   └── app.py                 # FastAPI backend with RAG functionality
├── templates/
│   └── index.html             # Hotel landing page HTML template
├── static/
│   └── style.css              # Additional CSS styles
├── data/
│   └── hotels details.pdf     # Hotel information PDF (auto-loaded)
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Google AI API key for Gemini | Yes |

### PDF Configuration

- **File Path**: `data/hotels details.pdf`
- **Auto-loading**: Enabled on server startup
- **Chunk Size**: 350 characters
- **Chunk Overlap**: 100 characters

### AI Model Settings

- **Embedding Model**: `models/embedding-001`
- **LLM Model**: `models/gemini-2.5-flash`
- **System Prompt**: Hotel concierge assistant role

## 🌟 Customization

### Modifying the Hotel Theme

1. **Update colors and branding**
   - Edit CSS variables in `templates/index.html`
   - Change logo text in the header
   - Update hero section background image

2. **Modify hotel features**
   - Edit the features section in `templates/index.html`
   - Add or remove feature cards
   - Update icons using Font Awesome classes

3. **Customize the chatbot**
   - Modify the system prompt in `src/app.py`
   - Adjust chunk size and overlap for text processing
   - Change the AI model (requires compatible API)

### Adding New Features

1. **New sections**
   - Add HTML sections to `templates/index.html`
   - Include corresponding CSS styles
   - Add navigation links if needed

2. **Enhanced chatbot**
   - Modify the RAG chain in `src/app.py`
   - Add conversation memory
   - Implement user authentication

## 🚀 Deployment

### Local Development
```bash
python -m uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload
```

### Production Deployment

1. **Use a production WSGI server** like Gunicorn
2. **Set up reverse proxy** with Nginx
3. **Configure environment variables** for API keys
4. **Enable HTTPS** with SSL certificates
5. **Set up monitoring** and logging

### Docker Deployment

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🐛 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **PDF upload fails** | Ensure `data/hotels details.pdf` exists and is readable |
| **Chatbot not responding** | Check if Google API key is set in `.env` file |
| **Server won't start** | Verify all dependencies are installed and port 8000 is available |
| **Import errors** | Ensure virtual environment is activated |

### Performance Optimization

1. **Large PDFs**
   - Reduce chunk size for better processing
   - Use smaller overlap values
   - Consider splitting very large documents

2. **Response time**
   - Optimize the embedding model
   - Use caching for frequent queries
   - Implement request rate limiting

## 🔒 Security Considerations

- **API Key Protection**: Never expose your Google AI API key in client-side code
- **File Upload**: Implement file type and size validation if adding upload functionality
- **Rate Limiting**: Add request throttling to prevent abuse
- **Input Validation**: Sanitize user inputs to prevent injection attacks
- **HTTPS**: Use SSL certificates in production
  

### Development Guidelines

- Follow PEP 8 Python style guidelines
- Add tests for new functionality
- Update documentation for API changes
- Ensure all tests pass before submitting PR


## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the amazing web framework
- [LangChain](https://langchain.com/) for the RAG framework
- [Google AI](https://ai.google.dev/) for the Gemini models
- [ChromaDB](https://www.trychroma.com/) for the vector database
- [Font Awesome](https://fontawesome.com/) for the beautiful icons


---

**⭐ Star this repository if you find it helpful!**

**Note**: This is a demonstration project. For production use in a real hotel, ensure proper security measures, data privacy compliance, and thorough testing. 
