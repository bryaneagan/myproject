from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Intro": "Hey Brodie"}

@app.get("/name/{nim}")
async def read_name(nim: int, name: Union[str, None] = None):
    return {"NIM": nim, "Name": name}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}