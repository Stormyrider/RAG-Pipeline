# TechNova Restricted RAG Pipeline

A professional, lightweight **Retrieval-Augmented Generation (RAG)** pipeline built with **Python, LangChain, OpenRouter, and Chroma**.

The system loads a controlled Markdown knowledge base, splits it into chunks, creates embeddings, stores them in Chroma, retrieves relevant context for a user question, and generates an answer using an OpenRouter-hosted LLM.

A key feature of this project is **knowledge-base restriction**: the assistant is instructed to answer only from the selected document and to refuse questions when the required information is not available in that knowledge base.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Key Features](#2-key-features)
3. [Technology Stack](#3-technology-stack)
4. [Project Structure](#4-project-structure)
5. [Prerequisites](#5-prerequisites)
6. [Installation & Setup (How to Run)](#6-installation--setup-how-to-run)
7. [API Configuration](#7-api-configuration)
8. [Knowledge Base](#8-knowledge-base)
9. [Document Loading](#9-document-loading)
10. [Chunking](#10-chunking)
11. [Chunking Experiment](#11-chunking-experiment)
12. [Embeddings](#12-embeddings)
13. [Vector Database](#13-vector-database)
14. [Retrieval](#14-retrieval)
15. [Context Generation](#15-context-generation)
16. [Restricted RAG Behavior](#16-restricted-rag-behavior)
17. [End-to-End RAG Pipeline](#17-end-to-end-rag-pipeline)
18. [Running the Project](#18-running-the-project)
19. [Employee Information Query Example](#19-employee-information-query-example)
20. [Why RAG Instead of Direct LLM Calls?](#20-why-rag-instead-of-direct-llm-calls)
21. [Why Chroma Instead of FAISS?](#21-why-chroma-instead-of-faiss)
22. [Security](#22-security)
23. [Current Limitations](#23-current-limitations)
24. [Learning Outcomes](#24-learning-outcomes)
25. [Quick Start](#25-quick-start)
26. [Final Architecture Summary](#26-final-architecture-summary)
27. [Conclusion](#27-conclusion)

---

## 1. Project Overview

Traditional LLM applications follow a simple, direct flow:

```text
User Question
      ↓
     LLM
      ↓
   Answer
```

This can be problematic when the model needs private, specialized, or frequently changing information that it was never trained on.

This project instead uses **Retrieval-Augmented Generation (RAG)**:

```text
                KNOWLEDGE BASE
                     │
                     ▼
                   LOAD
                     │
                     ▼
                  CHUNK
                     │
                     ▼
                EMBEDDING
                     │
                     ▼
                  CHROMA
                     │
                     │
              USER QUESTION
                     │
                     ▼
                 RETRIEVE
                     │
                     ▼
            RELEVANT CONTEXT
                     │
                     ▼
                  PROMPT
                     │
                     ▼
               OPENROUTER LLM
                     │
                     ▼
             ANSWER + SOURCE
```

The model receives retrieved information as context instead of relying only on its general knowledge, producing grounded, source-backed answers.

---

## 2. Key Features

- Markdown knowledge-base ingestion
- PDF and text loader support
- Recursive document chunking
- Configurable chunk size and overlap
- OpenRouter embeddings
- Chroma persistent vector store
- Semantic similarity retrieval
- LangChain prompt templates
- OpenRouter free-model routing for generation
- Source metadata and basic citations
- Restricted knowledge-base answering
- "Not available" fallback response when information is outside the selected document
- Local persistent vector database

---

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.13+ | Main programming language |
| LangChain | RAG orchestration |
| LangChain Chroma | Chroma integration |
| OpenRouter | Embeddings and LLM API |
| `openai/text-embedding-3-small` | Embedding model |
| `openrouter/free` | Free LLM routing |
| Chroma | Vector database |
| PyPDF | PDF document loading |
| python-dotenv | Environment-variable management |

---

## 4. Project Structure

```text
RAG project/
│
├── data/
│   ├── documents/
│   │   ├── python.md
│   │   ├── rag_notes.md
│   │   └── technova_knowledge.md
│   │
│   └── chroma/
│
├── src/
│   ├── loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── rag_pipeline.py
│   │
│   ├── test_loader.py
│   ├── test_chunker.py
│   ├── test_embeddings.py
│   ├── test_vector_store.py
│   ├── test_rag.py
│   ├── test_env.py
│   └── employee_query.py
│
├── experiments/
│   └── chunking_experiment.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

### Main Source Files

| File | Responsibility |
|---|---|
| `loader.py` | Loads PDF, Markdown, and text documents |
| `chunker.py` | Splits documents into smaller chunks |
| `embeddings.py` | Configures OpenRouter embeddings |
| `vector_store.py` | Stores and retrieves chunks using Chroma |
| `rag_pipeline.py` | Combines retrieval, prompting, generation, and sources |
| `chunking_experiment.py` | Compares chunk sizes and overlap values |
| `test_rag.py` | End-to-end pipeline test |
| `employee_query.py` | Example employee-information query |

---

## 5. Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.13+** — [Download Python](https://www.python.org/downloads/)
- **pip** (comes bundled with Python)
- A free **OpenRouter API key** — [Get one here](https://openrouter.ai/)
- Git (optional, only if cloning from a repository)

---

## 6. Installation & Setup (How to Run)

Follow these steps in order to get the project running from scratch.

### Step 1 — Open the project directory

Open a terminal / command prompt inside the project folder.

### Step 2 — Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

Current direct dependencies:

```text
langchain
langchain-chroma
langchain-openai
python-dotenv
pypdf
langchain-community
```

### Step 4 — Configure your API key

Create a `.env` file in the project root (see [Section 7](#7-api-configuration) for details).

### Step 5 — Run the pipeline

```bash
python src\test_rag.py
```

(On macOS/Linux use forward slashes: `python src/test_rag.py`)

That's it — the pipeline will load the knowledge base, build the vector store, and answer the sample questions defined in the script.

---

## 7. API Configuration

This project uses **OpenRouter** for both embeddings and LLM generation.

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

> ⚠️ Do not put the API key directly inside Python files.

The `.gitignore` file should contain:

```text
venv/
.env
__pycache__/
*.pyc
data/chroma/
```

This prevents the API key and local environment files from being committed accidentally.

**Never publish your API key in GitHub, screenshots, documentation, or chat messages.**

---

## 8. Knowledge Base

The main demonstration knowledge source is:

```text
data/documents/technova_knowledge.md
```

The document contains fictional information about:

- TechNova Solutions
- Employees
- Departments
- Joining dates
- Office hours
- Products
- Support policy
- Security policy

The restricted RAG demonstration uses this document as its controlled knowledge source.

### Example

The document contains:

```text
Ahmed works at TechNova Solutions as a Junior Software Engineer.
Ahmed joined the company in January 2026.
His department is Software Engineering.
```

A question such as:

```text
What department does Ahmed work in?
```

can therefore be answered from the knowledge base.

---

## 9. Document Loading

`loader.py` provides the document-loading layer.

Conceptually:

```text
PDF  → PyPDFLoader
MD   → TextLoader
TXT  → TextLoader
```

The loader returns LangChain `Document` objects containing:

```text
Document
├── page_content
└── metadata
```

Example metadata:

```python
{
    "source": "data/documents/technova_knowledge.md"
}
```

The metadata later supports source reporting.

---

## 10. Chunking

Large documents are split into smaller pieces before embedding.

The main chunker uses:

```python
RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
```

### Why chunking?

Chunking helps:

- Improve retrieval precision
- Keep retrieved context manageable
- Reduce unnecessary information sent to the LLM
- Preserve meaningful sections of documents

### Why overlap?

A small overlap helps preserve information around chunk boundaries.

Conceptually:

```text
Chunk 1:
[--------------------------]

              Chunk 2:
              [--------------------------]
              ↑
            overlap
```

---

## 11. Chunking Experiment

The project includes a small experiment that compares different configurations.

### Experiment Results

Using `rag_notes.md`:

| Chunk Size | Overlap | Number of Chunks |
|---:|---:|---:|
| 300 | 30 | 29 |
| 500 | 50 | 14 |
| 800 | 80 | 8 |

### Interpretation

- **300 / 30** creates more, smaller chunks and can provide more precise retrieval.
- **500 / 50** gives a balanced baseline for this project.
- **800 / 80** creates fewer, larger chunks and provides more surrounding context per result.

The project uses:

```text
chunk_size = 500
chunk_overlap = 50
```

as its default starting configuration.

These values are not universally optimal; chunking should be evaluated against the target documents and retrieval task.

**Run the experiment:**

```bash
python experiments\chunking_experiment.py
```

---

## 12. Embeddings

Embeddings convert text into numerical vectors representing semantic information.

Example:

```text
"Python is a programming language."
                ↓
         Embedding model
                ↓
[0.12, 0.84, 0.31, ...]
```

This project uses:

```text
openai/text-embedding-3-small
```

through OpenRouter.

The tested embedding vector size was:

```text
1536
```

The embedding workflow is:

```text
Chunk
  ↓
OpenRouter Embedding API
  ↓
Vector
```

---

## 13. Vector Database

The project uses **Chroma**.

Chroma stores:

```text
Chunk text
Embedding
Metadata
ID
```

The persistent database is stored in:

```text
data/chroma/
```

### Why Chroma?

Chroma is a practical choice for this project because it provides:

- Vector similarity search
- Persistent local storage
- Document storage
- Metadata handling
- Simple LangChain integration

FAISS would also be a strong option for high-performance vector similarity search, but Chroma is more convenient here because our application needs the vectors together with document text and metadata for a simple RAG workflow and source reporting.

---

## 14. Retrieval

When a user asks a question:

```text
User Question
      ↓
Question Embedding
      ↓
Chroma Similarity Search
      ↓
Top Relevant Chunks
```

The project retrieves the top `3` results:

```python
search(question, 3)
```

The retrieved document text is then combined into one context string.

---

## 15. Context Generation

The retrieved chunks are not stored as a separate context file. They are dynamically assembled in memory for each question.

The relevant logic is:

```python
documents = search(question, 3)

context = "\n\n".join(
    document.page_content for document in documents
)
```

Conceptually:

```text
Stored Chunks
     ↓
Similarity Search
     ↓
Retrieved Chunk 1
Retrieved Chunk 2
Retrieved Chunk 3
     ↓
      CONTEXT
     ↓
Prompt
```

This context is inserted into the LLM prompt.

---

## 16. Restricted RAG Behavior

The prompt explicitly tells the model:

```text
You are a restricted knowledge-base assistant.

Answer the question using only the information in the provided context.

Do not use outside knowledge or make assumptions.

If the answer is not contained in the context, say:
"The information is not available in the provided knowledge base."
```

This creates a controlled answering behavior.

### Supported Question

```text
Question:
What department does Ahmed work in?
```

Expected behavior:

```text
Software Engineering
```

### Unsupported Question

```text
Question:
Who is the president of Pakistan?
```

Expected behavior:

```text
The information is not available in the provided knowledge base.
```

This demonstrates that the model is being grounded in the selected knowledge base rather than answering from general knowledge.

---

## 17. End-to-End RAG Pipeline

The main workflow is implemented in `rag_pipeline.py`.

```text
                     ┌──────────────────────┐
                     │ technova_knowledge.md│
                     └──────────┬───────────┘
                                │
                                ▼
                           Document Loader
                                │
                                ▼
                             Chunking
                                │
                                ▼
                         OpenRouter Embedding
                                │
                                ▼
                              Chroma
                                │
                                │
                         User Question
                                │
                                ▼
                         Similarity Search
                                │
                                ▼
                        Retrieved Documents
                                │
                                ▼
                         Context Construction
                                │
                                ▼
                         Prompt Template
                                │
                                ▼
                         OpenRouter LLM
                                │
                                ▼
                         Answer + Sources
```

---

## 18. Running the Project

### End-to-End Test

From the project root:

```bash
python src\test_rag.py
```

#### Example supported query

```text
What department does Ahmed work in?
```

Example result:

```text
Answer:
Software Engineering

Sources:
- data/documents/technova_knowledge.md
```

#### Example unsupported query

```text
Who is the president of Pakistan?
```

Example result:

```text
Answer:
The information is not available in the provided knowledge base.

Sources:
- data/documents/technova_knowledge.md
```

---

## 19. Employee Information Query Example

The project also includes an employee-focused example.

Run:

```bash
python src\employee_query.py
```

The example asks:

```text
What is Ahmed's department, job title, and joining date?
```

The answer is generated through the same retrieval pipeline and is grounded in the TechNova knowledge base.

---

## 20. Why RAG Instead of Direct LLM Calls?

A direct LLM application is:

```text
Question → LLM → Answer
```

The RAG system is:

```text
Question
   ↓
Retrieve evidence
   ↓
Question + evidence
   ↓
LLM
   ↓
Grounded answer
```

RAG is useful when the application needs:

- Private knowledge
- Specialized documentation
- Frequently updated information
- Searchable company data
- Source-aware answers

---

## 21. Why Chroma Instead of FAISS?

Both Chroma and FAISS can perform vector similarity search.

### FAISS

FAISS is excellent for:

- Fast vector indexing
- Nearest-neighbor search
- Large-scale similarity-search workloads
- Highly optimized local vector search

### Chroma

Chroma is convenient for this project because it combines:

- Vector storage
- Document text
- Metadata
- Persistence
- Simple LangChain integration

Our project is a relatively small, controlled RAG knowledge base where we need source information along with retrieved chunks.

Therefore:

```text
Chroma → simpler project architecture
FAISS  → excellent lower-level vector search option
```

For this implementation, Chroma is the more convenient choice.

---

## 22. Security

### Never commit API keys

Make sure `.env` is ignored by Git:

```text
.env
```

### If a key is exposed

Immediately revoke/rotate the key at the provider and replace it locally.

### Do not hard-code secrets

Avoid:

```python
api_key = "secret-key"
```

Use environment variables instead:

```python
os.getenv("OPENROUTER_API_KEY")
```

---

## 23. Current Limitations

This project is a clean educational/prototype RAG implementation. A production system would normally add:

- Retrieval similarity thresholds
- Richer citation information
- Page numbers for PDFs
- Document IDs and chunk IDs
- Duplicate-document handling
- Automated evaluation
- Logging and monitoring
- API/backend authentication
- User interface
- Error handling for provider outages
- Production vector infrastructure when scale requires it

The current implementation demonstrates the core RAG architecture clearly without unnecessary complexity.

---

## 24. Learning Outcomes

This project demonstrates understanding of:

- Why RAG is used
- RAG architecture
- Document loading
- Chunking
- Chunk overlap
- Embeddings
- Vector databases
- Similarity search
- Metadata
- Retrieval
- Prompt templates
- Context injection
- Grounded generation
- Source reporting
- Restricted knowledge-base answering

---

## 25. Quick Start

```bash
# 1. Create and activate environment
python -m venv venv
venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure API key in .env
# OPENROUTER_API_KEY=your_key

# 4. Run end-to-end RAG test
python src\test_rag.py
```

---

## 26. Final Architecture Summary

```text
                  TECHNOVA KNOWLEDGE BASE
                           │
                           ▼
                        LOADER
                           │
                           ▼
                        CHUNKER
                      500 / 50
                           │
                           ▼
                  OPENROUTER EMBEDDINGS
                           │
                           ▼
                         CHROMA
                           │
                    ┌──────┴──────┐
                    │             │
             User Question     Stored Vectors
                    │             │
                    └──────┬──────┘
                           ▼
                      RETRIEVAL
                           │
                           ▼
                   RELEVANT CONTEXT
                           │
                           ▼
                    RESTRICTED PROMPT
                           │
                           ▼
                  OPENROUTER FREE LLM
                           │
                           ▼
                   ANSWER + SOURCES
```

---

## 27. Conclusion

This project implements a complete Retrieval-Augmented Generation pipeline using LangChain, OpenRouter, and Chroma.

The pipeline does not simply send a question directly to an LLM. It first retrieves relevant information from a controlled knowledge base, places that information into the prompt, and then generates an answer from the retrieved context.

The final implementation demonstrates both the **retrieval** and **generation** sides of RAG while maintaining a simple project structure that is easy to understand, test, and extend.
