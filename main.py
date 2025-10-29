"""
Louis Forget 405 TP3
"""

import random

niveau_de_vie = 20
play_game = True
showed_rules = False
force_adversaire1 = 0
force_adversaire2 = 0
nombre_de_monstres = 0
puissance_attaque1 = 0
puissance_attaque2 = 0
monstres_battus = 0
adversaire_boss = 0

while play_game:
    if not showed_rules:
        force_adversaire1 = random.randint(1, 5)
        force_adversaire2 = random.randint(1, 3)
        nombre_de_monstres = random.randint(1, 2)
        adversaire_boss = random.randint(3, 5)
    if monstres_battus == 3:
        nombre_de_monstres = 0
        print(f"un boss apparait devant vous! il a {adversaire_boss} points de vies")
    if monstres_battus == 4:
        nombre_de_monstres = 0
        print(f"un boss apparait devant vous! il a {adversaire_boss} points de vies")
    if nombre_de_monstres == 1:
        print(f"vous avez {niveau_de_vie} point de vie et votre adversaire en a {force_adversaire1}")
    elif nombre_de_monstres == 2:
        print(f"vous avez {niveau_de_vie} points de vies, deux adversaires se trouvent dans la prochaine piece \n"
              f"le premier a {force_adversaire1} point de vies et le deuxieme en a {force_adversaire2}")

    action = input("Que voulez vous faire?\n"
                   "1- Combattre cet adversaire\n"
                   "2- Contournez cet adversaire et aller ouvrir une autre porte (-1 pv)\n"
                   "3- Afficher les regles du jeu \n"            
                   "4- Quitter la partie")
    if action == "1":

        if monstres_battus == 3:
            nombre_de_monstres = -1
            puissance_attaque1 = random.randint(1, 6)
            print(f"vous roulez un {puissance_attaque1} ")

        if monstres_battus == 4:
            nombre_de_monstres = -1
            puissance_attaque1 = random.randint(1, 6)
            print(f"vous roulez un {puissance_attaque1} pour attaquer le boss!")

            if puissance_attaque1 > adversaire_boss:
                print("vous avez battu un boss!")
                niveau_de_vie += adversaire_boss
                niveau_de_vie += adversaire_boss
                print(f"vous avez maintenant {niveau_de_vie} point de vie!")

            else:
                print("le boss etait trop fort pour vous")
                niveau_de_vie -= adversaire_boss
                print(f"vous avez maintenant {niveau_de_vie} point de vie!")
                monstres_battus = 0

            monstres_battus = 0

        if nombre_de_monstres == 1:
            puissance_attaque1 = random.randint(1, 6)
            print(f"vous roulez un {puissance_attaque1} ")

            if puissance_attaque1 > force_adversaire1:
                print("vous venez a bout de votre adversaire!")
                niveau_de_vie += force_adversaire1
                print(f"vous avez maintenant {niveau_de_vie} point de vie!")
                monstres_battus += 1

            else:
                print("vous n avez pas ete a la hauteur")
                niveau_de_vie -= force_adversaire1
                print(f"vous avez maintenant {niveau_de_vie} point de vie!")

        elif nombre_de_monstres == 2:
            puissance_attaque1 = random.randint(1, 6)
            puissance_attaque2 = random.randint(1, 6)
            print(f"vous roulez un {puissance_attaque1} et un {puissance_attaque2}")

            if puissance_attaque1 > force_adversaire1:
                print("vous etes venus a bout du monstre #1")
                niveau_de_vie += force_adversaire1
                monstres_battus += 1

            else:
                print("le monstre #1 etait trop fort pour vous")
                niveau_de_vie -= force_adversaire1

            if puissance_attaque2 > force_adversaire2:
                print("vous etes venus a bout du monstre #2")
                niveau_de_vie += force_adversaire2
                monstres_battus += 1

            else:
                print("le monstre #2 etait trop fort pour vous")
                niveau_de_vie -= force_adversaire2

    elif action == "2":
        niveau_de_vie -= 1
        print(f"point de vie restant:{niveau_de_vie}")
    elif action == "3":
        showed_rules = True
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.\n"
              "Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n"
              "Une défaite a lieu lorsque la valeur du dé lancé est inférieure ou égale à la force de l’adversaire.\n"
              "Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n"
              "La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n"
              "L’usager peut combattre ou éviter chaque adversaire, \n"
              " dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")
    elif action == "4":
        play_game = False

    if niveau_de_vie <= 0:
        print("vous avez perdu tous vos points de vies")
        play_game = False
