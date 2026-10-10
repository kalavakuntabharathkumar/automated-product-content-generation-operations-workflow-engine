from pydantic import BaseModel, Field
from typing import Literal

class Product(BaseModel):
    sku: str
    name: str
    features: list[str] = Field(default_factory=list)
    category: str
    tone: Literal["professional", "friendly", "luxury", "playful"] = "professional"

class GeneratedContent(BaseModel):
    sku: str
    title: str
    description: str
    tone: str
    approved: bool = False
