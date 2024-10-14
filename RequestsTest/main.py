import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1b2962316aa8a8d272595c6fe7096032'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
body_create = {
    "name" : "generate",
    "photo_id" : -1
}
body_change ={
    "pokemon_id": "86490",
    "name": "GHYJUK",
    "photo_id": 204
}
body_add ={
    "pokemon_id": "86490"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_add.text)