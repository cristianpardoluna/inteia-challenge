import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def created_test_book():
    data = {
        "title": "Cien años de soledad",
        "author": "Gabriel García Márquez",
        "year": 1967
    }
    response = client.post(
        "/libros/",
        json=data
    )
    assert response.status_code == 200
    response_data = response.json()
    assert data["title"] == response_data["title"]
    assert data["year"] == response_data["year"]
    return response_data

def test_create_book(created_test_book):
    pass

def test_list_books():
    """ Prueba unitaria para el listado de libros
    """
    params = {
        "title": "años",
    }
    response = client.get(
        "/libros/",
        params=params
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data) > 0

def test_retrieve_book(created_test_book):
    """ Prueba unitaria para retorno de libro por ID
    """
    book_id = created_test_book["id"]
    response = client.get(
        f"/libros/{book_id}"
    )
    assert response.status_code == 200

def test_book_not_found():
    """ Prueba unitaria para manejo ID no encontrado
    """
    book_id = "NO EXISTE"
    response = client.get(
        f"/libros/{book_id}"
    )
    assert response.status_code == 404

def test_update_book(created_test_book):
    """ Prueba unitaria para actualizar (PUT) libro
    """
    book_id = created_test_book["id"]
    data = {
        "title": "El coronel no tiene quien le escriba",
        "author": created_test_book["author"],
        "year": 1961
    }
    response = client.put(
        f"/libros/{book_id}",
        json=data
    )
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["title"] == data["title"]
    assert response_data["year"] == data["year"]

def test_delete_book(created_test_book):
    """ Prueba unitaria para eliminación de libros
    """
    book_id = created_test_book["id"]
    response = client.delete(
        f"/libros/{book_id}"
    )
    assert response.status_code == 204
