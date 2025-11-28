
import os

from workflow import create_graph
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from twilio.rest import Client

load_dotenv(override=True)

app = FastAPI(title="WhatsApp Bot API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou sua lista de domínios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class RequestBody(BaseModel):
    user_name: str
    user_number: str


@app.post("/send_twilio_template")
async def send_twilio_template(body: RequestBody):
    """
    Sent initial template
    """

    
    account_sid = os.environ.get("ACCOUNT_SID")
    auth_token = os.environ.get("AUTH_TOKEN")
    content_sid = os.environ.get("CONTENT_SID")
    from_number = os.environ.get("FROM_NUMBER")
    to_number = body.user_number
    user_name = body.user_name
    client = Client(account_sid, auth_token)

    client.messages.create(
        from_=f'whatsapp:{from_number}',
        content_sid=content_sid,
        content_variables=f'{"1":{user_name}}',
        to=f'whatsapp:+{to_number}'
    )
    
    return {}

@app.post("/reply_whatsapp")
async def reply_whatsapp(request: Request):
    
    payload = await request.form()
    message = payload.get("Body")
    sender = payload.get("From")
    graph = create_graph()
    
    initial_state = {
        "messages": [{"role":"user", "content":message}],
        "user_number": sender
    }
    
    await graph.ainvoke(initial_state)

    return {}


@app.post("/hello")
def hello():
    return {}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

