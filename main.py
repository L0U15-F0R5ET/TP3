"""
Louis Forget 405 TP3
"""

import random

niveau_de_vie = 20
play_game = True


while play_game:
    while showed_rules:
        force_adversaire = random.randint(1, 5)
    print(f"vous avez {niveau_de_vie} point de vie et votre adversaire en a {force_adversaire}")
    action = input("Que voulez vous faire?\n"
                   "1- Combattre cet adversaire\n"
                   "2- Contournez cet adversaire et aller ouvrir une autre porte (-1 pv)\n"
                   "3- Afficher les regles du jeu \n"            
                   "4- Quitter la partie")
    if action == "1":
        puissance_attaque = random.randint(1, 6)
        print(f"vous roulez un {puissance_attaque} ")

        if puissance_attaque > force_adversaire:
            print("vous venez a bout de votre adversaire!")
            niveau_de_vie += force_adversaire
            print(f"vous avez maintenant {niveau_de_vie} point de vie!")
        else:

            print("vous n avez pas ete a la hauteur")
            niveau_de_vie -= force_adversaire
            print(f"vous avez maintenant{niveau_de_vie} point de vie")

    elif action == "2":
        niveau_de_vie -= 1
        print(f"point de vie restant:{niveau_de_vie}")
    elif action == "3":
        showed_rules = True
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.\n"
              "Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n"
              "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.\n"
              "Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n"
              "La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n"
              "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")
    elif action == "4":
        play_game = False






