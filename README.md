---
title: LawMadad
emoji: 👀
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
---

# ⚖️ LawMadad-Model

LawMadad is a specialized AI-powered Pakistani Legal Assistant designed to provide structured, accurate, and context-aware guidance based on the Pakistani legal framework. Built using FastAPI and LlamaIndex, it leverages RAG (Retrieval-Augmented Generation) to query a comprehensive database of Pakistani laws, including civil, criminal, family, and constitutional codes.

## 🚀 Features

- **Legal RAG Pipeline**: Efficiently retrieves relevant legal clauses from a large corpus of PDF documents.
- **Intelligent Query Classification**: Automatically distinguishes between general greetings, capability inquiries, and complex legal queries.
- **Structured Legal Responses**: Provides detailed analysis including Introduction, Section Descriptions, Legal Provisions, Punishments, Precedents, and Recommendations.
- **Groq Acceleration**: Powered by Llama 3.1 8B on Groq for lightning-fast inference.
- **Confidence Scoring**: Internally calculates similarity scores to ensure high-quality information retrieval.

## 🛠 Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **LLM**: [Groq](https://groq.com/) (Llama 3.1 8B Instant)
- **Engine**: [LlamaIndex](https://www.llamaindex.ai/)
- **Embeddings**: HuggingFace (`sentence-transformers/all-MiniLM-L6-v2`)
- **Containerization**: [Docker](https://www.docker.com/)

---

## 📥 Getting Started

### Prerequisites

- Python 3.9 or higher
- [Groq API Key](https://console.groq.com/)
- Docker (optional, for containerized deployment)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd LawMadad-Model
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🏃 Running the Application

### Locally

Start the FastAPI server using Uvicorn:

```bash
python app.py
```
Or:
```bash
uvicorn app:app --host 0.0.0.0 --port 7860
```

The API will be available at `http://localhost:7860`.

### With Docker

1. **Build the image**:
   ```bash
   docker build -t lawmadad-model .
   ```

2. **Run the container**:
   ```bash
   docker run -p 7860:7860 --env GROQ_API_KEY=your_groq_api_key_here lawmadad-model
   ```

---

## 📡 API Documentation

### Root Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns a simple welcome message and usage instructions.

### Query Endpoint
- **URL**: `/query/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "query": "What is the punishment for theft under the Pakistan Penal Code?"
  }
  ```
- **Response**:
  ```json
  {
    "response": "1. **Introduction/Overview**: Theft is defined under Section 378 of the PPC...\n..."
  }
  ```

---

## 📁 Project Structure

```text
.
├── app.py              # Main FastAPI application & RAG logic
├── Dockerfile          # Containerization for HF Spaces
├── requirements.txt    # Python dependencies
├── storage_law_app/    # Persisted LlamaIndex vector store
├── .github/workflows/  # CI/CD for Hugging Face deployment
└── *.pdf               # Pakistani legal corpus (Data source)
```

---

## 🚀 Deployment

The project is configured for automated deployment to **Hugging Face Spaces**.

### GitHub Actions
- **Deploy**: On every push to the `master` branch, the `deploy.yml` workflow pushes the code to the [ali4568/LawMadad](https://huggingface.co/spaces/ali4568/LawMadad) Space.
- **Sync Env**: The `sync_env_to_huggingface.yml` workflow ensures environment variables like `GROQ_API_KEY` are synchronized.

---

## 📚 Data Corpus

The model is powered by a comprehensive set of legal documents, including:
- Constitution of Pakistan
- Pakistan Penal Code (PPC)
- Civil Procedure Code (CPC)
- Family Law Ordinance
- Property & West Family Laws
- And various other specialized legal drafts.

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---
*Note: This application is intended for educational and informational purposes. Always consult with a qualified legal professional for actual legal advice.*