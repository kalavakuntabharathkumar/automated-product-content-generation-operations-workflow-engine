import json, os
from openai import AsyncOpenAI
from .schemas import Product, GeneratedContent

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def generate_content(product: Product) -> GeneratedContent:
    prompt = f"""Return JSON with sku,title,description,tone,approved.
Do not invent specifications. Product: {product.model_dump_json()}"""
    response = await client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        response_format={"type": "json_object"},
        messages=[
            {"role":"system","content":"Write concise factual e-commerce catalog copy."},
            {"role":"user","content":prompt}
        ],
    )
    result = GeneratedContent.model_validate(json.loads(response.choices[0].message.content))
    result.sku = product.sku
    result.approved = tone_check(result)
    return result

def tone_check(content: GeneratedContent) -> bool:
    text=(content.title+" "+content.description).lower()
    return not any(word in text for word in ["guaranteed","miracle","fake"])
