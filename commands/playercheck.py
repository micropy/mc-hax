import requests
import sys

def mojangapi(username):
    api = f'https://api.mojang.com/users/profiles/minecraft/{username}'
    response = requests.get(api)
    infojson = response.json()
    if response.status_code == 200:
        print(f'username: {infojson["name"]}\nuuid: {infojson["id"]}')
mojangapi(sys.argv[1])