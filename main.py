"""
Louis Forget 405 TP3
"""

import random

niveau_de_vie = 20

force_adversaire = random.randint(1, 5)

action = input("Que voulez vous faire?\n"
               "1- Combattre cet adversaire\n"
               "2- Contournez cet adversaire et aller ouvrir une autre porte (-1 pv)\n"
               "3- Quitter la partie")
