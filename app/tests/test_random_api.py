import pytest
from fastapi.testclient import TestClient
from fastapi import HTTPException
from main import app
import string


@pytest.fixture
def test_client():
    return TestClient(app)


def test_get_root(test_client):
    response = test_client.get("/random/")
    assert response.status_code == 200
    assert "float" in response.json()
    assert 0 <= response.json()["float"] <= 1


def test_get_random_int(test_client):
    response = test_client.get("/random/int")
    assert response.status_code == 200
    assert "int" in response.json()


@pytest.mark.parametrize("left, right, status_code", [
    (1, 10, 200),
    (10, 1, 400),
    (-10, 10, 200)
])
def test_get_random_in_range(test_client, left, right, status_code):
    response = test_client.get(f"/random/int/{left}/{right}")
    assert response.status_code == status_code
    if status_code == 200:
        assert "int" in response.json()
        assert left <= response.json()["int"] <= right


def test_get_random_char(test_client):
    response = test_client.get("/random/char")
    assert response.status_code == 200
    assert "char" in response.json()
    assert response.json()["char"] in string.ascii_letters


def test_toss_coin(test_client):
    response = test_client.get("random/coinflip")
    assert response.status_code == 200
    assert "result" in response.json()
    assert response.json()["result"] in ["Heads", "Tails"]


@pytest.mark.parametrize("options,status_code", [
    ('["a", "b", "c"]', 200),
    ('[]', 400),
    ('["Ronaldo"]', 200),
    ('["Harry Potter"]', 200),
])
def test_get_random_option(test_client, options, status_code):
    response = test_client.get(f"/random/select/{options}")
    assert response.status_code == status_code
    if response.status_code == 200:
        assert "selected" in response.json()
        assert response.json()["selected"] in options

def test_get_color(test_client):
    response = test_client.get("/random/color")
    assert response.status_code == 200
    assert "color" in response.json()
    assert response.json()["color"].startswith("#")
    assert len(response.json()["color"]) == 7


def test_get_user(test_client):
    response = test_client.get("/random/user")
    assert response.status_code == 200
    user = response.json()
    assert "name" in user
    assert "email" in user
    assert "password" in user


@pytest.mark.parametrize("length,status_code", [
    (8, 200),
    (0, 400),
    (-1, 400),
    (3, 400),
    (4, 200),
    (12, 200),
])
def test_get_password(test_client, length, status_code):
    response = test_client.get(f"/random/password/{length}")
    assert response.status_code == status_code
    if status_code == 200:
        assert "password" in response.json()
        assert len(response.json()["password"]) == max(0, length)