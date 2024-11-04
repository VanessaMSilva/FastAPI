from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def teste_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "lala"}


def teste_criar_valores():
    response = client.get("/menu/")
    assert response.status_code == 201
    assert "Mensagens" in response.json()  
    assert isinstance(response.json()["Mensagens"], list) 


def teste_get_horarios():
    response = client.get("/Horario/")
    assert response.status_code == 200
    data = response.json()
    assert "horariosChegada050" in data 
    assert "horariosSaidaIntercampi" in data 
    assert isinstance(data["horariosChegada050"], list) 
    assert isinstance(data["horariosSaidaIntercampi"], list)

def teste_buscar_valores():
    response = client.get("/mensagens")
    assert response.status_code == 200
    assert isinstance(response.json(), list) 
    for mensagem in response.json():
        assert "menuNav" in mensagem  
        assert "link" in mensagem 
