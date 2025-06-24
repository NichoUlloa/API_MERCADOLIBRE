import os, sys
sys.path.append(os.path.dirname(__file__))
from fastapi import FastAPI, Depends
from deps_ml import ml_search, ml_item

app = FastAPI(title="ML Recommender")

@app.get("/search")
async def search(q: str, price: str | None = None):
    return await ml_search(q, price)

@app.get("/item/{item_id}")
async def item(item_id: str):
    return await ml_item(item_id)

@app.get("/auth")
async def auth():
    return {"detail": "OAuth flow placeholder"}
