import requests


class Name:


    def __init__(self, name):
            self.name = name
    
    def name_input(self, name):
        req = requests.get(f'https://api.agify.io?name={name}')

        show = req.json()
        print('Name:' , show['name'], 'Age: ', show['age'])

        """req anropar API:n som sedan hämtar tillbaks informationen som läggs till i show som sedan skrivs ut"""

user = Name('namn')

user_input = ''
while user_input != 'exit':
    check = True
    while check == True:
        user_input = str(input('Skriv ett namn: '))

        if len(user_input) >= 30:
            print('\nnamnet du skrev in är för långt, försök igen.\n')
        
        else:
            check = False
    
    if user_input == 'exit':
        break

    user.name_input(user_input)

    """användaren får skriva in ett namn till user_input som sedan kollas av en if-sats ifall namnet är för lång med hjälp av en bool.
       Ifall namnet är rätt längd skickas den in i metoden name_input"""