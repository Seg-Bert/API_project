import requests


req = requests.get('https://api.agify.io?name=Fredrik')
class Name:
    def __init__(self, name):
            self.name = name

show = req.json()

print(show)