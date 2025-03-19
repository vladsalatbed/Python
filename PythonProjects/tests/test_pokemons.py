import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fec437644889509fe23aa2c8a58f3b91'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '22781'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'togedemaru'


@pytest.mark.parametrize('key, value', [('name', 'togedemaru'), ('trainer_id', TRAINER_ID), ('id', '203371')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value 