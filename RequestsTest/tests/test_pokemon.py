import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1b2962316aa8a8d272595c6fe7096032'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 7700

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params={'level':3})
    assert response.status_code ==200

def test_name():
    response_get = requests.get(url = f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"]=='Красотка'

