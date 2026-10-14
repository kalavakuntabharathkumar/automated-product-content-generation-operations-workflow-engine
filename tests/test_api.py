from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)

def test_health():
    assert client.get("/health").json()["status"]=="ok"

def test_product_validation():
    r=client.post("/api/content/generate",json={
        "sku":"SKU-1","name":"Desk Lamp","category":"Lighting",
        "features":["LED"],"tone":"friendly"
    })
    assert r.status_code in (200,502)
