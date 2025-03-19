import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fec437644889509fe23aa2c8a58f3b91'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_registarrtion = {
    "trainer_token": TOKEN,
    "email": "podaskarbinom@gmail.com",
    "password": "MastersSync1"
}
body_confirmation = {
    "trainer_token": TOKEN,
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": "12"
}
'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registarrtion )
print(response.text)'''

'''response_confirmation = requests.post (url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post (url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)