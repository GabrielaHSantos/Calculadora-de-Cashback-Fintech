from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Cashback API is running"}

def test_calcular_cashback_endpoint():
    payload = {
        "tipo_cliente": "VIP",
        "valor_compra": 600,
        "desconto_pct": 20
    }
    response = client.post("/calcular", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["valor_final"] == 480
    assert data["cashback"] == 26.4

def test_historico_endpoint():
    # Faz um cálculo primeiro para ter histórico
    client.post("/calcular", json={
        "tipo_cliente": "Regular",
        "valor_compra": 100,
        "desconto_pct": 0
    })
    
    response = client.get("/historico")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1
