import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'eee38be42ade01c4e3459492fc4cd791'
HEADER = {'Content-Type' : 'application/json ', 'trainer_token' : TOKEN}
TRAINER_ID = '4898'

def test_vilkastatuscode():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200



def test_trainerid():
    response_get_ = response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get_.json() ['data'][0]["trainer_id"] == '4898'