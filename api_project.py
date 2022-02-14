import requests


class Name:
    def __init__(self, name):
            self.name = name
    
    def name_input(self, name):
        req = requests.get(f'https://api.agify.io?name={name}')
        show = req.json()
        print('Name:' , show['name'], 'Age: ', show['age'])


user = Name('namn')

user_input = ''
while user_input != 'exit':
    user_input = str(input('Skriv ett namn: '))
    if user_input == 'exit':
        break
    user.name_input(user_input)