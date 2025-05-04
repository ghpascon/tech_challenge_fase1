import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, Mock
from bs4 import BeautifulSoup
from mock import mocks
from app.main import app
from app.routes import embrapa

client = TestClient(app)

def override_get_current_user():
    return {"username": "test_user"}

app.dependency_overrides[embrapa.get_current_user] = override_get_current_user

@pytest.fixture
def mock_response():
    mock = Mock()
    mock.text = mocks.mock_html1()
    return mock

def mock_response_2():
    mock = Mock()
    mock.text = mocks.mock_html2()
    return mock


def fake_get_json(soup: BeautifulSoup):
    return {"titulo": "Fake Table", "total": 10}


def fake_get_json2(soup: BeautifulSoup):
    return {"titulo": "Fake Table 2", "total": 20}

@patch("app.routes.embrapa.requests.get")
@patch("app.routes.embrapa.get_json", side_effect=fake_get_json)
def test_producao(mock_get_json, mock_requests_get, mock_response):
    mock_requests_get.return_value = mock_response
    response = client.get("/embrapa/producao?ano=2020")
    assert response.status_code == 200
    assert response.json()["titulo"] == "Produção de vinhos, sucos e derivados"

@patch("app.routes.embrapa.requests.get")
@patch("app.routes.embrapa.get_json", side_effect=fake_get_json)
def test_processamento(mock_get_json, mock_requests_get, mock_response):
    mock_requests_get.return_value = mock_response
    response = client.get("/embrapa/processamento?ano=2020")
    assert response.status_code == 200
    assert response.json()["total"] == 1831171480

@patch("app.routes.embrapa.requests.get")
@patch("app.routes.embrapa.get_json", side_effect=fake_get_json)
def test_comercializacao(mock_get_json, mock_requests_get, mock_response):
    mock_requests_get.return_value = mock_response
    response = client.get("/embrapa/comercializacao?ano=2020")
    assert response.status_code == 200
    assert "titulo" in response.json()

@patch("app.routes.embrapa.requests.get")
@patch("app.routes.embrapa.get_json2", side_effect=fake_get_json2)
def test_importacao(mock_get_json2, mock_requests_get, mock_response):
    mock_requests_get.return_value = mock_response_2()
    response = client.get("/embrapa/importacao?ano=2020")
    assert response.status_code == 200
    assert response.json()["total"] == 688564355

@patch("app.routes.embrapa.requests.get")
@patch("app.routes.embrapa.get_json2", side_effect=fake_get_json2)
def test_exportacao(mock_get_json2, mock_requests_get, mock_response):
    mock_requests_get.return_value = mock_response_2()
    response = client.get("/embrapa/exportacao?ano=2020")
    assert response.status_code == 200
    assert response.json()["total"] == 550851484
