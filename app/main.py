from fastapi import FastAPI
from .schemas import Product, GeneratedContent
from .llm import generate_content

app=FastAPI(title="Product Content Workflow Engine", version="1.0.0")

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/api/content/generate", response_model=GeneratedContent)
async def generate(product: Product):
    return await generate_content(product)
