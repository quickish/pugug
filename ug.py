from typing import Optional

from fastapi import FastAPI

app = FastAPI()
tem=[]

@app.get("/")
def read_root():
    return tem


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/webhook")
def webhook (item):
    print(item)
    return {"success": True}


@app.post("/webhook/uplink")
def uplink (item: dict):
    print(item)
    tem.append(item)
    return {"success": True}