# WhatsApp Bot API

An intelligent WhatsApp chatbot powered by AI that processes user questions and responds via WhatsApp messages using the Infobip API. The bot leverages LangGraph workflows, OpenAI agents, and Tavily search capabilities to provide comprehensive answers.

## 🎯 Project Goal

This project aims to create an automated WhatsApp chatbot that:
- Receives questions from users via API
- Processes questions using AI agents with web search capabilities (Tavily)
- Generates intelligent responses using GPT-4.1-mini
- Sends responses back to users via WhatsApp using Infobip

## 🚀 Technologies

### Core Framework
- **FastAPI** (0.121.3) - Modern, fast web framework for building APIs
- **Uvicorn** (0.38.0) - ASGI server for running FastAPI applications

### AI & Workflow
- **LangGraph** (1.0.3) - Framework for building stateful, multi-actor applications with LLMs
- **OpenAI Agents** (0.6.1) - Library for creating AI agents with OpenAI models
- **Tavily** - Web search API integrated via MCP (Model Context Protocol) for real-time information retrieval

### Data & Validation
- **Pydantic** (2.12.4) - Data validation using Python type annotations

### Utilities
- **python-dotenv** (1.2.1) - Loads environment variables from `.env` files

### External Services
- **Infobip API** - WhatsApp messaging service
- **OpenAI GPT-4.1-mini** - Language model for generating responses

## 📋 API Endpoints

### POST `/answer_something`

Processes a user question and sends the AI-generated response via WhatsApp.

**Request Body:**
```
{
  "question": "What is the weather like today?",
  "user_number": "+1234567890"
}
```
**Response:**son
```
{
  "success_info": "Message sent successful!",
  "failed_info": ""
}
```
**Description:**
- Accepts a user question and phone number
- Processes the question through a LangGraph workflow
- Uses an AI agent with Tavily search to generate a comprehensive answer
- Sends the response to the user's WhatsApp number via Infobip

### POST `/send_template`

Sends an initial WhatsApp template message to a user.

**Request Body:**
```
{
  "question": "",
  "user_number": "+1234567890"
}
```
```
**Response:**son
{
  "success_info": "Message sent successful!",
  "failed_info": ""
}
````

**Description:**
- Sends a predefined WhatsApp template message
- Used for initial user engagement or welcome messages

## 🏗️ Architecture

The application uses a **LangGraph workflow** with the following structure:

1. **Process Node** (`process_message`)
   - Receives user question
   - Initializes AI agent with Tavily MCP server for web search
   - Generates response using GPT-4.1-mini
   - Returns processed state with AI response

2. **Send WhatsApp Node** (`send_whatsapp_message`)
   - Extracts the final message from the processed state
   - Sends the message to the user via Infobip WhatsApp API


## 🔧 Setup & Installation

### Prerequisites
- Python 3.12+
- Infobip API credentials
- OpenAI API key
- Tavily API key

### Installation Steps

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
   INFOBIP_API_KEY=your_infobip_api_key
   BASE_URL=https://your-infobip-base-url
   SENDER_NUMBER=your_whatsapp_sender_number
   TAVILY_API_KEY=your_tavily_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

5. **Run the application**
   ```bash
   python main.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

6. **Access API documentation**
   
   Once running, visit:
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

## 📁 Project Structure

```
whatsapp_bot/
├── api/
│   ├── main.py           # FastAPI application and endpoints
│   ├── nodes.py          # LangGraph node functions
│   ├── workflow.py       # LangGraph workflow definition
│   ├── client.py         # Infobip WhatsApp client
│   ├── requirements.txt  # Python dependencies
│   └── .env              # Environment variables (not in repo)
└── README.md
```

## 🔐 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `INFOBIP_API_KEY` | Infobip API authentication key | Yes |
| `BASE_URL` | Infobip API base URL | Yes |
| `SENDER_NUMBER` | WhatsApp sender number | Yes |
| `TAVILY_API_KEY` | Tavily search API key | Yes |
| `OPENAI_API_KEY` | OpenAI API key | Yes |

## 🧪 Usage Example

### Using cURL

**Send a question:**
```bash
curl -X POST "http://localhost:8000/answer_something" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What is artificial intelligence?",
    "user_number": "+1234567890"
  }'
```

**Send template:**
```bash
curl -X POST "http://localhost:8000/send_template" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "",
    "user_number": "+1234567890"
  }'
```


## 🔄 How It Works

1. **User sends question** → API receives POST request with question and phone number
2. **Workflow initialization** → LangGraph workflow is created and initialized
3. **Message processing** → AI agent processes the question with web search capabilities
4. **Response generation** → GPT-4.1-mini generates a comprehensive answer
5. **WhatsApp delivery** → Response is sent to user via Infobip WhatsApp API
