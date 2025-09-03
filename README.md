# HR Leave Policy Chatbot

An AI-powered HR assistant that answers employee queries about company leave policies using RAG (Retrieval-Augmented Generation) technology.

## Features

- **Document Processing**: Extracts text from PowerPoint files including OCR for images
- **Vector Search**: Uses FAISS vector database for efficient document retrieval
- **AI-Powered Responses**: Leverages Groq's Llama-3.3-70b model for accurate answers
- **Strict Policy Adherence**: Only provides information from the official leave policy document
- **RESTful API**:FastAPI backend with CORS support for web applications
 

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd backend
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Install Tesseract OCR (Windows):

- Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)

- Set path in pytesseract.pytesseract.tesseract_cmd

4. Set up environment variables:
Create a .env file in the root directory with your Groq API key:
```bash
GROQ_API_KEY=your_groq_api_key_here
```
**Usage**:

Prepare your document: Place your PowerPoint leave policy file in the **/data** directory

Run the application:
```bash
python main.py
```
**Access the API**: 

The server will start on  http://127.0.0.1:8000

**API Endpoints** :
```http
GET / - Health check endpoint
```

```http
POST /chat - Main chatbot endpoint

Request body: {"query": "your question here"}
```
