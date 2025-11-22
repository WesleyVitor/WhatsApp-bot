

from workflow import create_graph
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

from client import InfobipClient
load_dotenv(override=True)

app = FastAPI(title="WhatsApp Bot API", version="1.0.0")

class RequestBody(BaseModel):
    question: str
    user_number: str

class ResponseBody(BaseModel):
    success_info: str
    failed_info: str

@app.post("/answer_something")
async def answer_something(body: RequestBody):
    """
    Endpoint to call chatbot
    """
    graph = create_graph()
    
    initial_state = {
        "messages": [{"role":"user", "content":body.question}],
        "user_number": body.user_number
    }
    
    await graph.ainvoke(initial_state)

    return ResponseBody(success_info="Message sent successful!")

@app.post("/send_template")
async def send_template(body: RequestBody):
    """
    Sent initial template
    """
    client = InfobipClient()
    client.send_initial_template(body.user_number)
    
    return ResponseBody(success_info="Message sent successful!")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

