# Agentic Graph RAG AI Knowledge Assistant
## Complete Project Documentation

**Project Created:** 2026-07-09  
**Status:** Early-stage (Alpha - ~30% complete)  
**Difficulty Level:** Advanced (5/5) ⭐⭐⭐⭐⭐

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Architecture & Flow](#architecture--flow)
3. [Core Concepts](#core-concepts)
4. [Project Structure](#project-structure)
5. [File Inventory](#file-inventory)
6. [Knowledge Base Categories](#knowledge-base-categories)
7. [Current Implementation](#current-implementation)
8. [Issues & TODO](#issues--todo)
9. [Tech Stack](#tech-stack)
10. [Development Roadmap](#development-roadmap)

---

## Project Overview

### Problem Statement
Developers face fragmentation when searching for answers across documentation, notes, and knowledge graphs. This project aims to unify the developer knowledge workflow by providing an AI assistant that retrieves relevant context, reasons over graph relationships, and answers queries with grounded references.

### Solution
An integrated AI system that combines:
- **RAG (Retrieval-Augmented Generation)** - Finds relevant context from knowledge base
- **Vector Search** - Semantic similarity matching using embeddings
- **Knowledge Graph** - Represents relationships between concepts
- **Agent Orchestration** - Multi-step reasoning and task execution
- **LLM Integration** - Generates answers grounded in retrieved context

### Target Users
- Software developers seeking quick answers
- Students learning technical concepts
- Documentation researchers
- ML/AI practitioners

---

## Architecture & Flow

### System Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    USER QUERY                               │
│            (e.g., "Explain Python basics")                  │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
        ┌──────────────────────┐
        │  FRONTEND (Chat UI)  │  ← Web interface for users
        │  (React)             │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  BACKEND (API)       │  ← FastAPI/Flask server
        │  RESTful endpoints   │
        └──────────┬───────────┘
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
   ┌─────────┐         ┌──────────────┐
   │ AGENT   │         │ RETRIEVAL    │
   │ (Brain) │────────▶│ (Search)     │
   │ Multi-  │         │              │
   │ step    │         └──────┬───────┘
   │ reasoning         │
   └────┬────┘         ▼
        │        ┌──────────────────┐
        │        │  VECTOR STORE    │
        │        │  (Chroma/FAISS)  │
        │        │                  │
        │        │  - Embeddings    │
        │        │  - Doc index     │
        │        └────────┬─────────┘
        │                 │
        │        ┌────────▼──────────┐
        │        │ KNOWLEDGE BASE    │
        │        │ - PDFs            │
        │        │ - Documents       │
        │        │ - Code snippets   │
        │        └────────┬──────────┘
        │                 │
        │        ┌────────▼──────────┐
        │        │ GRAPH DATABASE    │
        │        │ - Concepts        │
        │        │ - Relationships   │
        │        │ - Dependencies    │
        │        └───────────────────┘
        │
        ▼
   ┌──────────────────────┐
   │ LLM (OpenAI)         │  ← Answer generation
   │                      │
   │ - Processes context  │
   │ - Reasons over data  │
   │ - Generates answers  │
   └──────────┬───────────┘
              │
              ▼
   ┌──────────────────────┐
   │ FORMATTED RESPONSE   │
   │ - Answer text        │
   │ - Source references  │
   │ - Related concepts   │
   └──────────────────────┘
```

---

## Core Concepts

### 1. RAG (Retrieval-Augmented Generation)
**Definition:** Providing LLMs with retrieved context before generating answers.

**Why it matters:**
- Prevents hallucinations (LLM sticks to actual data)
- Provides up-to-date information
- Enables source citations
- Reduces computational cost

**Flow:**
```
Query → Retrieve Relevant Docs → Feed to LLM → Answer with References
```

### 2. Vector Store & Embeddings
**Definition:** Converting text into high-dimensional vectors for similarity search.

**How it works:**
1. PDF documents are loaded
2. Text is split into chunks (1000 chars, 200 overlap)
3. Each chunk is converted to embeddings (using OpenAI)
4. Embeddings stored in Chroma vector database
5. User queries converted to embeddings and matched with documents

**Tools Used:**
- **Chroma:** Vector database for persistent storage
- **FAISS:** Alternative lightweight vector search
- **OpenAI Embeddings:** State-of-the-art embedding models

### 3. Knowledge Graph
**Definition:** A network representing concepts and their relationships.

**Example structure:**
```
Python ──uses─→ Variables
Python ──uses─→ Functions
Variables ──instance_of─→ Data_Types
Functions ──returns─→ Values
```

**Benefits:**
- Multi-hop reasoning (follow relationships)
- Concept discovery (related topics)
- Knowledge organization
- Semantic understanding

### 4. Agent Orchestration
**Definition:** Autonomous systems that break complex tasks into steps.

**Example task: "Compare Python and Java"**
```
Agent Plan:
  Step 1: Query "Python advantages in ML"
  Step 2: Query "Java limitations in ML"
  Step 3: Use LLM to synthesize comparison
  Step 4: Format and return answer
```

**Capabilities:**
- Multi-step reasoning
- Tool usage (search, calculate, fetch)
- Context management
- Error recovery

### 5. Backend API
**Definition:** RESTful server exposing core functionality.

**Planned Endpoints:**
- `POST /api/ingest` - Add documents to knowledge base
- `POST /api/query` - Ask a question
- `GET /api/documents` - List indexed documents
- `GET /api/graph/concepts` - Browse knowledge graph
- `POST /api/agent/task` - Execute multi-step task

---

## Project Structure

```
agentic-graph-rag-ai-knowledge-assistant/
│
├── LICENSE                           # MIT License
├── README.md                         # Project overview
├── requirements.txt                  # Python dependencies
│
├── ingestion/                        # Document loading & processing
│   ├── __init__.py
│   ├── loader.py                    # PDF loader
│   ├── splitter.py                  # Text chunking
│   └── run_ingestion.py             # Ingestion pipeline
│
├── retrieval/                        # Search & RAG
│   ├── __init__.py
│   ├── retriever.py                 # Query interface
│   └── vector_store.py              # Chroma/FAISS management
│
├── backend/                          # REST API (Empty - TODO)
│   └── [FastAPI application]
│
├── frontend/                         # UI (Empty - TODO)
│   └── [React application]
│
├── agent/                           # Agent system (Empty - TODO)
│   └── [Multi-step reasoning]
│
├── graph/                           # Knowledge graph (Empty - TODO)
│   └── [Graph construction]
│
├── llm/                             # LLM integration (Empty - TODO)
│   └── [OpenAI/local LLM wrapper]
│
├── knowledge_base/                  # Domain documents
│   ├── AI/                          # Artificial Intelligence
│   ├── ANN/                         # Artificial Neural Networks
│   ├── AWS/                         # Amazon Web Services
│   ├── Computer_Networks/           # Networking concepts
│   ├── Data_Mining_Warehousing/     # Data engineering
│   ├── DBMS/                        # Database management
│   ├── Deep_Learning/               # Deep learning concepts
│   ├── DSA/                         # Data Structures & Algorithms
│   ├── Java/                        # Java programming
│   ├── LangChain/                   # LangChain framework
│   ├── Machine_Learning/            # ML algorithms & theory
│   ├── NLP/                         # Natural language processing
│   ├── Operating_System/            # OS concepts
│   ├── Python/                      # Python programming
│   ├── RAG/                         # RAG systems
│   ├── RL/                          # Reinforcement Learning
│   ├── SQL/                         # SQL & databases
│   └── Theory_of_computation/       # CS theory
│
├── config/                          # Configuration files (Empty - TODO)
│   └── settings.py
│
├── utils/                           # Shared utilities (Empty - TODO)
│   └── helpers.py
│
├── tests/                           # Testing suite (Empty - TODO)
│   └── test_*.py
│
└── vector_db/                       # Persisted vector store (Generated)
    └── [Chroma database files]
```

---

## File Inventory

### Core Implementation Files

#### 1. ingestion/loader.py
**Purpose:** Load PDF documents from knowledge_base directories

**Key Functions:**
- `list_pdf_paths(root_dir)` - Find all PDFs recursively
- `load_documents(root_dir)` - Load PDFs and create Document objects

**Features:**
- Recursive directory traversal
- Metadata extraction (source file, path)
- Batch loading support

**Status:** ✅ Complete

```python
from pathlib import Path
from typing import List

from langchain.document_loaders import PyPDFLoader
from langchain.schema import Document


def list_pdf_paths(root_dir: Path) -> List[Path]:
    """Find all PDF files in root_dir and subdirectories."""
    return sorted(root_dir.rglob("*.pdf"))


def load_documents(root_dir: Path) -> List[Document]:
    """Load all PDF documents from root_dir, maintaining metadata."""
    root_dir = Path(root_dir)
    documents: List[Document] = []

    for pdf_path in list_pdf_paths(root_dir):
        loader = PyPDFLoader(str(pdf_path))
        pdf_docs = loader.load()
        for doc in pdf_docs:
            metadata = dict(doc.metadata)
            metadata["source_file"] = str(pdf_path.relative_to(root_dir))
            metadata["source_path"] = str(pdf_path)
            documents.append(Document(page_content=doc.page_content, metadata=metadata))

    return documents


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent / "knowledge_base"
    docs = load_documents(root)
    print(f"Loaded {len(docs)} document chunks from {root}")
```

#### 2. ingestion/splitter.py
**Purpose:** Split large documents into searchable chunks

**Key Functions:**
- `split_documents(documents)` - Chunk documents with overlap

**Configuration:**
- Chunk size: 1000 characters
- Overlap: 200 characters (maintains context across chunks)

**Status:** ✅ Complete

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from typing import List


def split_documents(documents: List[Document], chunk_size: int = 1000, chunk_overlap: int = 200) -> List[Document]:
    """Split documents into chunks with overlap for context preservation."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)


if __name__ == "__main__":
    print("Use ingestion/run_ingestion.py to load, split, and store documents.")
```

#### 3. ingestion/run_ingestion.py
**Purpose:** Orchestrate the complete ingestion pipeline

**Pipeline Steps:**
1. Load all PDFs from knowledge_base/
2. Split into chunks
3. Create embeddings and build vector store
4. Persist to disk

**Status:** ✅ Complete

```python
from pathlib import Path

from ingestion.loader import load_documents
from ingestion.splitter import split_documents
from retrieval.vector_store import build_vector_store


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    data_dir = repo_root / "knowledge_base"
    persist_dir = repo_root / "vector_db"

    print("Loading PDF documents from:", data_dir)
    documents = load_documents(data_dir)
    print(f"Loaded {len(documents)} documents from PDFs.")

    print("Splitting documents into chunks...")
    chunks = split_documents(documents)
    print(f"Created {len(chunks)} text chunks.")

    print("Building Chroma vector store...")
    build_vector_store(chunks, persist_dir)
    print("Vector store persisted to:", persist_dir)


if __name__ == "__main__":
    main()
```

#### 4. retrieval/vector_store.py
**Purpose:** Manage vector database creation and querying

**Key Functions:**
- `build_vector_store()` - Create embeddings and store vectors
- `load_vector_store()` - Load persisted vector database

**Database:** Chroma (persistent, local, easy to use)

**Status:** ⚠️ Has syntax error (needs fixing)

```python
from pathlib import Path
from typing import List

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document


def build_vector_store(documents: List[Document], persist_directory: Path, collection_name: str = "knowledge_base") -> Chroma:
    """Create vector store from documents using OpenAI embeddings."""
    persist_directory = Path(persist_directory)
    persist_directory.mkdir(parents=True, exist_ok=True)

    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(
        documents,
        embeddings,
        persist_directory=str(persist_directory),
        collection_name=collection_name,
    )
    db.persist()
    return db


def load_vector_store(persist_directory: Path, collection_name: str = "knowledge_base") -> Chroma:
    """Load existing vector store from disk."""
    embeddings = OpenAIEmbeddings()
    db = Chroma(
        persist_directory=str(persist_directory),
        collection_name=collection_name,
        embedding_function=embeddings,
    )
    return db


if __name__ == "__main__":
    print("Use retrieval/retriever.py or ingestion/run_ingestion.py to run the vector store pipeline.")
```

#### 5. retrieval/retriever.py
**Purpose:** Query interface for semantic search

**Key Functions:**
- `query_store()` - Search for similar documents

**Status:** ✅ Complete

```python
from pathlib import Path
from typing import List

from langchain.schema import Document

from retrieval.vector_store import load_vector_store


def query_store(query_text: str, persist_directory: Path, k: int = 4) -> List[Document]:
    """Query the vector store for k most similar documents."""
    db = load_vector_store(persist_directory)
    return db.similarity_search(query_text, k=k)


if __name__ == "__main__":
    persist_dir = Path(__file__).resolve().parent.parent / "vector_db"
    query_text = "Explain the basics of Python programming."
    docs = query_store(query_text, persist_dir)
    for i, doc in enumerate(docs, 1):
        print(f"--- Result {i} ---")
        print(doc.page_content[:400].strip())
        print("metadata:", doc.metadata)
        print()
```

#### 6. run_ingestion.py (Root Level)
**Purpose:** Convenience script at project root

**Status:** ✅ Complete

```python
from pathlib import Path

from ingestion.loader import load_documents
from ingestion.splitter import split_documents
from retrieval.vector_store import build_vector_store


def main() -> None:
    repo_root = Path(__file__).resolve().parent
    data_dir = repo_root / "knowledge_base"
    persist_dir = repo_root / "vector_db"

    print("Loading PDF documents from:", data_dir)
    documents = load_documents(data_dir)
    print(f"Loaded {len(documents)} documents from PDFs.")

    print("Splitting documents into chunks...")
    chunks = split_documents(documents)
    print(f"Created {len(chunks)} text chunks.")

    print("Building Chroma vector store...")
    build_vector_store(chunks, persist_dir)
    print("Vector store persisted to:", persist_dir)


if __name__ == "__main__":
    main()
```

### Configuration Files

#### requirements.txt
**Purpose:** Python dependencies

**Status:** ✅ Complete

```
fastapi
uvicorn
openai
langchain
chromadb
pypdf
faiss-cpu
python-dotenv
pytest
```

#### .gitignore
**Typically excludes:**
- vector_db/ (persisted embeddings)
- __pycache__/ (compiled Python)
- .env (API keys)
- .venv/ (virtual environment)

#### LICENSE
**Type:** MIT License  
**Usage:** Open-source, permissive, minimal restrictions

---

## Knowledge Base Categories

### 18 Domain Categories

| Category | Purpose |
|----------|---------|
| **AI** | Artificial Intelligence fundamentals |
| **ANN** | Artificial Neural Networks |
| **AWS** | Amazon Web Services documentation |
| **Computer_Networks** | Networking concepts & protocols |
| **Data_Mining_Warehousing** | ETL & data engineering |
| **DBMS** | Database management systems |
| **Deep_Learning** | Deep neural networks & frameworks |
| **DSA** | Data structures & algorithms |
| **Java** | Java programming language |
| **LangChain** | LangChain framework & examples |
| **Machine_Learning** | ML algorithms & theory |
| **NLP** | Natural language processing |
| **Operating_System** | OS concepts & systems |
| **Python** | Python programming & best practices |
| **RAG** | RAG systems & implementations |
| **RL** | Reinforcement learning |
| **SQL** | SQL queries & database design |
| **Theory_of_computation** | CS theory & complexity |

---

## Current Implementation

### ✅ Completed Components

1. **Ingestion Pipeline** (100%)
   - PDF loading and processing
   - Text chunking with overlap
   - Document metadata handling

2. **Retrieval System** (80%)
   - Vector store creation
   - Similarity search interface
   - Query functionality

3. **Project Structure**
   - All directories created
   - Knowledge base organized
   - Config structure ready

### ❌ TODO Components

1. **Backend API** (0%)
   - FastAPI application
   - RESTful endpoints
   - Request validation
   - Error handling

2. **Frontend UI** (0%)
   - React chat interface
   - Document browser
   - Result display
   - Styling & UX

3. **Agent System** (0%)
   - Multi-step reasoning
   - Tool orchestration
   - Context management
   - Response formatting

4. **Knowledge Graph** (0%)
   - Graph database setup
   - Concept extraction
   - Relationship modeling
   - Graph traversal

5. **LLM Integration** (0%)
   - OpenAI wrapper
   - Prompt engineering
   - Response generation
   - Citation handling

6. **Testing** (0%)
   - Unit tests
   - Integration tests
   - E2E tests

---

## Issues & TODO

### 🐛 Known Issues

**Issue 1: Syntax Error in vector_store.py (Line 3)**
```
Current: from langchain.embe import Documentddings.openai import OpenAIEmbeddings
Problem: Malformed import statement
Solution: Should be: from langchain.embeddings.openai import OpenAIEmbeddings
```

**Issue 2: Missing Environment Setup**
- OPENAI_API_KEY not configured
- Vector database not initialized

**Issue 3: No Error Handling**
- Ingestion lacks validation
- Retrieval lacks timeout handling

### 📋 Development Roadmap

**Phase 1: Fix & Test (Week 1)**
- [ ] Fix syntax errors
- [ ] Install dependencies
- [ ] Test ingestion pipeline
- [ ] Verify vector store creation

**Phase 2: Backend (Week 2-3)**
- [ ] Implement FastAPI server
- [ ] Create /ingest endpoint
- [ ] Create /query endpoint
- [ ] Add authentication
- [ ] Add rate limiting

**Phase 3: Frontend (Week 3-4)**
- [ ] Create React chat UI
- [ ] Implement query interface
- [ ] Add result display
- [ ] Add document browser

**Phase 4: Agent System (Week 5)**
- [ ] Implement multi-step reasoning
- [ ] Add tool orchestration
- [ ] Create task definitions
- [ ] Add response formatting

**Phase 5: Graph Integration (Week 6)**
- [ ] Setup graph database
- [ ] Extract concepts
- [ ] Model relationships
- [ ] Implement graph queries

**Phase 6: Testing & Deployment (Week 7-8)**
- [ ] Write comprehensive tests
- [ ] Document API
- [ ] Setup CI/CD
- [ ] Deploy to production

---

## Tech Stack

### Backend
- **Python 3.9+** - Primary language
- **FastAPI** - REST API framework
- **Uvicorn** - ASGI server
- **LangChain** - LLM orchestration
- **Chroma** - Vector database
- **FAISS** - Alternative vector search
- **OpenAI API** - Embeddings & LLM

### Frontend
- **React 18+** - UI framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Axios** - HTTP client

### Database
- **Chroma** - Vector store (primary)
- **FAISS** - Vector search (optional)
- **Neo4j** - Knowledge graph (planned)
- **PostgreSQL** - Metadata (optional)

### DevOps
- **Docker** - Containerization
- **GitHub Actions** - CI/CD
- **Pytest** - Testing framework
- **Black** - Code formatting
- **Pylint** - Linting

---

## Development Roadmap

### Long-term Vision
1. **Year 1: MVP**
   - Core RAG functionality
   - Basic agent capabilities
   - Simple frontend UI

2. **Year 2: Enhancement**
   - Advanced graph features
   - Multi-model support
   - Better reasoning

3. **Year 3: Scale**
   - Production deployment
   - Commercial features
   - Integration with tools

### Success Metrics
- Response accuracy > 90%
- Query latency < 2 seconds
- User retention > 60%
- Community contributions growing

---

## Getting Started

### Prerequisites
- Python 3.9+
- OpenAI API key
- 2GB RAM minimum
- 1GB disk space

### Installation
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set environment variables
setx OPENAI_API_KEY "your_key_here"

# 3. Place PDFs in knowledge_base/
# (Put your PDFs in respective category folders)

# 4. Run ingestion pipeline
python ingestion/run_ingestion.py

# 5. Test retrieval
python retrieval/retriever.py
```

### First Run
```bash
# Terminal 1: Start backend
uvicorn backend.main:app --reload

# Terminal 2: Test query
curl -X POST http://localhost:8000/api/query \
  -H "Content-Type: application/json" \
  -d '{"query": "Explain RAG"}'
```

---

## Conclusion

This is a comprehensive, well-architected project combining cutting-edge AI technologies. The foundation is solid, and the next steps focus on building the missing components (Backend, Frontend, Agent System, Graph Integration).

**Ready to develop? Next steps:**
1. Fix syntax errors
2. Test ingestion pipeline
3. Build backend API
4. Implement frontend UI

**Questions?** Refer to README.md or code comments in each module.

---

**Document Generated:** July 9, 2026  
**Project Status:** Early-stage, Active Development  
**License:** MIT (Open Source)

