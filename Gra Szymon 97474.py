import random

game = list()
game = ['kamien', 'papier', 'nozyce']

randomChoice = random.choice(game)

option = input("Wybierz: \n1.Kamień \n2.Papier \n3.Nożyce \nPodaj liczbe: ")

print(f'Wybór wroga: {randomChoice}')

if option == "1":
    if randomChoice == "kamien":
        print('remis')
    elif randomChoice == "papier":
        print('przegrałeś')
    elif randomChoice == "nozyce":
        print('wygrałeś')
elif option == "2":
    if randomChoice == "kamien":
        print('wygrałeś')
    elif randomChoice == "papier":
        print('remis')
    elif randomChoice == "nozyce":
        print('przegrałeś')
elif option == "3":
    if randomChoice == "kamien":
        print('przegrałeś')
    elif randomChoice == "papier":
        print('wygrałeś')
    elif randomChoice == "nozyce":
        print('remis')