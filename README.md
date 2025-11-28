# WhatsApp Bot

An intelligent WhatsApp chatbot powered by AI that processes user questions and responds via WhatsApp messages using the Twilio API. The bot leverages LangGraph workflows, OpenAI agents, and Tavily search capabilities to provide comprehensive answers.

## 🎯 Project Overview

This project is an automated WhatsApp chatbot that:
- Receives messages from users via WhatsApp webhook
- Processes questions using AI agents with web search capabilities (Tavily)
- Generates intelligent responses using GPT-4.1-mini
- Sends responses back to users via WhatsApp using Twilio

## ✨ Features

### Core Features
- **AI-Powered Conversations**: Uses OpenAI GPT-4.1-mini to generate intelligent, contextual responses
- **Web Search Integration**: Leverages Tavily search API via MCP (Model Context Protocol) for real-time information retrieval
- **LangGraph Workflow**: Stateful, multi-step processing pipeline for handling complex conversations
- **WhatsApp Integration**: Seamless messaging via Twilio WhatsApp API
- **Template Messaging**: Support for sending initial template messages to users
- **Webhook Support**: Receives and processes incoming WhatsApp messages in real-time

### Technical Features
- **FastAPI Backend**: Modern, high-performance API framework
- **Asynchronous Processing**: Non-blocking message processing for better performance
- **State Management**: LangGraph manages conversation state across workflow steps
- **CORS Enabled**: Ready for frontend integration

## 🚀 Technologies

### Backend Framework
- **FastAPI** (0.121.3) - Modern, fast web framework for building APIs
- **Uvicorn** (0.38.0) - ASGI server for running FastAPI applications

### AI & Workflow
- **LangGraph** (1.0.3) - Framework for building stateful, multi-actor applications with LLMs
- **OpenAI Agents** (0.6.1) - Library for creating AI agents with OpenAI models
- **Tavily** - Web search API integrated via MCP (Model Context Protocol) for real-time information retrieval

### Messaging
- **Twilio** (9.8.7) - WhatsApp messaging service for sending and receiving messages

### Data & Validation
- **Pydantic** (2.12.4) - Data validation using Python type annotations

### Utilities
- **python-dotenv** (1.2.1) - Loads environment variables from `.env` files

### Frontend
- **Next.js** (16.0.4) - React framework for building the UI
- **React** (19.2.0) - UI library
- **Tailwind CSS** (4.x) - Utility-first CSS framework
- **TanStack Query** (5.90.11) - Data fetching and state management

## 🏗️ Architecture

The application uses a **LangGraph workflow** with the following structure:

1. **Process Node** (`process_message`)
   - Receives user question from WhatsApp
   - Initializes AI agent with Tavily MCP server for web search
   - Generates response using GPT-4.1-mini
   - Returns processed state with AI response

2. **Send WhatsApp Node** (`send_whatsapp_message`)
   - Extracts the final message from the processed state
   - Sends the message to the user via Twilio WhatsApp API

### Key Endpoints

The API includes two main endpoints:

- **Template Endpoint**: Sends initial WhatsApp template messages to users
- **Webhook Endpoint**: Receives incoming WhatsApp messages and triggers the AI workflow to generate and send responses

## 🔧 Setup & Installation

### Prerequisites
- Python 3.12+
- Node.js 18+ (for frontend)
- Twilio account with WhatsApp API access
- OpenAI API key
- Tavily API key

### Backend Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd whatsapp_bot
   ```

2. **Create a virtual environment**
   ```bash
   cd api
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the `api` directory:
   ```env
   ACCOUNT_SID=your_twilio_account_sid
   AUTH_TOKEN=your_twilio_auth_token
   CONTENT_SID=your_twilio_content_template_sid
   FROM_NUMBER=your_twilio_whatsapp_number
   TAVILY_API_KEY=your_tavily_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

5. **Run the backend**
   ```bash
   python main.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

### Frontend Installation

1. **Navigate to UI directory**
   ```bash
   cd ui
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Run the development server**
   ```bash
   npm run dev
   ```

4. **Access the application**
   - Frontend: `http://localhost:3000`
   - API Documentation: `http://localhost:8000/docs`

## 📁 Project Structure


```
whatsapp_bot/
├── api/
│   ├── main.py           # FastAPI application and endpoints
│   ├── nodes.py          # LangGraph node functions
│   ├── workflow.py       # LangGraph workflow definition
│   ├── requirements.txt  # Python dependencies
│   └── .env              # Environment variables (not in repo)
├── ui/
│   ├── app/              # Next.js app directory
│   ├── public/           # Static assets
│   ├── package.json      # Node.js dependencies
│   └── ...
└── README.md
```

## 🔐 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `ACCOUNT_SID` | Twilio Account SID | Yes |
| `AUTH_TOKEN` | Twilio Authentication Token | Yes |
| `CONTENT_SID` | Twilio Content Template SID | Yes |
| `FROM_NUMBER` | Twilio WhatsApp sender number | Yes |
| `TAVILY_API_KEY` | Tavily search API key | Yes |
| `OPENAI_API_KEY` | OpenAI API key | Yes |

## 🔄 How It Works

1. **User sends message** → WhatsApp message is received via webhook endpoint
2. **Workflow initialization** → LangGraph workflow is created and initialized with the user's message
3. **Message processing** → AI agent processes the question with web search capabilities using Tavily
4. **Response generation** → GPT-4.1-mini generates a comprehensive answer based on the search results
5. **WhatsApp delivery** → Response is automatically sent to the user via Twilio WhatsApp API

## 🎨 Frontend

The project includes a Next.js frontend application for managing and interacting with the WhatsApp bot. The UI is built with:
- Modern React components
- Tailwind CSS for styling
- TanStack Query for efficient data fetching
- Responsive design
