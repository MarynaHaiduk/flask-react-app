import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Flask API is running!"


def test_health(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json == {
        "status": "OK"
    }


def test_get_products(client):
    response = client.get("/api/products")
    assert response.status_code == 200
    products = response.json
    assert isinstance(products, list)
    assert len(products) == 3
    assert products[0]["id"] == 1
    assert products[0]["name"] == "Laptop"


def test_get_product(client):
    response = client.get("/api/products/1")
    assert response.status_code == 200
    product = response.json
    assert product["id"] == 1
    assert product["name"] == "Laptop"
    assert product["price"] == 1299.99


def test_get_product_2(client):
    response = client.get("/api/products/2")
    assert response.status_code == 200
    product = response.json
    assert product["id"] == 2
    assert product["name"] == "Smartphone"


def test_product_not_found(client):
    response = client.get("/api/products/999")
    assert response.status_code == 404
    assert response.json == {
        "error": "Product not found"
    }