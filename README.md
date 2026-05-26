# AI Operating System

An intelligent multi-agent AI Operating System built using LangGraph, FastAPI, Next.js, and Retrieval-Augmented Generation (RAG).

This project combines:
- AI agents
- task orchestration
- document understanding
- memory
- vector search
- PDF ingestion
- conversational UI

into a single AI-powered system.

---

# Features

## Multi-Agent Architecture

The system uses multiple specialized agents:

- Planner Agent
- Research Agent
- RAG Agent
- Calculator Agent
- Chatbot Agent

---

## LangGraph Orchestration

Uses LangGraph for:
- workflow orchestration
- conditional routing
- multi-agent execution
- shared state management

---

## RAG Pipeline

Supports:
- PDF uploads
- document chunking
- embeddings generation
- vector retrieval
- contextual answering

---

## AI Chat Interface

Frontend built with:
- Next.js
- TypeScript
- Tailwind CSS
- shadcn/ui

Features:
- modern chat UI
- chat sidebar
- multiple conversations
- PDF upload system

---

# Tech Stack

## Frontend
- Next.js
- TypeScript
- Tailwind CSS
- shadcn/ui

## Backend
- FastAPI
- LangGraph
- LangChain
- Groq API

## AI / RAG
- HuggingFace Embeddings
- ChromaDB
- Sentence Transformers

---

# Project Architecture

```bash
Frontend (Next.js)
        ↓
FastAPI Backend
        ↓
LangGraph Workflow
        ↓
AI Agents / Tools
        ↓
RAG + Vector Database
```

---

# Folder Structure

```bash
backend/
│
├── rag/
│   ├── embeddings.py
│   ├── loader.py
│   ├── splitter.py
│   ├── vectorstore.py
│   ├── rag.py
│
├── nodes.py
├── graph.py
├── state.py
├── app.py
│
└── uploads/


frontend/
│
├── app/
├── components/
├── services/
├── store/
├── hooks/
└── types/
```

---

# Installation

## Clone Repository




---

# Backend Setup

```bash
cd backend
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Backend

```bash
uvicorn app:app --reload
```

---

# Frontend Setup

```bash
cd frontend
```

## Install Dependencies

```bash
npm install
```

## Run Frontend

```bash
npm run dev
```

---

# Environment Variables

Create a `.env` file inside backend:

```env
GROQ_API_KEY=your_api_key
```

---

# Current Capabilities

- Conversational AI
- Multi-agent workflows
- Web research
- PDF uploads
- RAG retrieval
- Vector search
- Chat history UI
- Memory integration
- Tool routing

---

# Future Improvements

- Streaming responses
- MongoDB persistence
- pgvector migration
- Voice support
- Authentication
- Better retrieval (MMR / reranking)
- Hybrid search
- Multi-user support

---

# Learning Outcomes

This project demonstrates:
- AI orchestration
- LangGraph workflows
- RAG systems
- vector databases
- AI agent architecture
- FastAPI backend development
- Next.js frontend architecture
- full-stack AI engineering



# Author

Karan
