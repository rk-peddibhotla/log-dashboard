from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import redis

app = FastAPI()

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/messages")
def get_messages():
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    msg = f"New message at {now}"
    r.lpush("messages", msg)
    r.ltrim("messages", 0, 19)
    messages = r.lrange("messages", 0, 19)
    return {"messages": messages}
