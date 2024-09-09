import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'eee38be42ade01c4e3459492fc4cd791'
HEADER = {'Content-Type' : 'application/json ', 'trainer_token' : TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}


body_put = {
    "pokemon_id": "69441",
    "name": "Ковальски",
    "photo_id": 4
}

body_add = {
    "pokemon_id": "69441"
}




'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''



'''response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put)
print(response_name.text)'''



'''response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_pokeball.text)
'''



