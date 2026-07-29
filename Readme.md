# PDF ChatBot

A smart, conversational PDF assistant built with Python and LangChain. This project lets you chat with the contents of a PDF document using Retrieval-Augmented Generation (RAG), making it possible to ask questions about a document and receive grounded, context-aware answers.

## 🌟 Features

- Upload and query PDF content interactively
- Uses LangChain for document processing and retrieval
- Converts PDF text into vector embeddings for semantic search
- Stores and retrieves relevant chunks with FAISS
- Generates answers using Google Gemini
- Clean, modular project structure for easy extension

## 🛠️ Tech Stack

- Python
- LangChain
- LangChain Community
- FAISS
- Google Gemini API
- Python-dotenv

## 📂 Project Structure

```text
Pdf-ChatBot/
│
├── app.py                  # Main entry point for the chatbot
├── requirements.txt       # Python dependencies
├── data/                  # PDF documents folder
├── faiss_index/           # Persisted FAISS vector index
├── utils/                 # Helper modules for splitting, embedding, retrieval, and chaining
│   ├── chain.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── splitter.py
│   └── vectorstore.py
└── Readme.md
```

## 🚀 Getting Started

### 1. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root and add your Google API key:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

### 4. Add your PDF file

Place the PDF you want to chat with inside the `data/` folder. By default, the app uses:

```text
data/resume.pdf
```

If you want to use a different file, update the path in `app.py`.

### 5. Run the application

```bash
python app.py
```

You will be prompted to enter your question. Type `exit` to quit the program.

## 🧠 How It Works

1. The PDF is loaded using a document loader.
2. The text is split into smaller chunks.
3. Each chunk is converted into embeddings.
4. The embeddings are stored in a FAISS vector index.
5. When a question is asked, the most relevant chunks are retrieved.
6. A Gemini-powered LLM generates a response grounded in the retrieved context.

## ⚙️ Configuration Notes

- To change the number of retrieved chunks, edit `utils/retriever.py`.
- To change the chunk size and overlap, edit `utils/splitter.py`.
- To change the embedding or LLM model, update the relevant files in the `utils/` folder.

## ✨ Example Usage

```text
Ask: What is this candidate's experience?
```

The assistant will respond based only on the information available in the PDF context.

## 📌 Notes

- The app relies on a valid Google Gemini API key.
- The response quality depends on the quality and structure of the PDF content.
- This project is a great starting point for building more advanced document Q&A systems.

## 🤝 Contributing

Contributions are welcome. If you have ideas for improving the chatbot, feel free to open an issue or submit a pull request.
   