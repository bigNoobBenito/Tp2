"""
Ce code a été fait par Benito Karol Yehouenou le 29 Septembre 2022
Groupe:
Ce code est un jeu de devinette qui demande a l'utilisateur de deviner le nombre que l'ordinateur a choisit
C'est l'utilisateur qui decide jusqu'ou est ce que l'ordinateur peut choisir ses nombres
"""

import random


def choosing_number():
    """
    Cette fonction demande a l'utilisateur le nombre qu'il peut choisir parmi une range de nombre
    :return: le nombre aléatoire choisis
    """
    range1 = int(input("vous devez choisir entre deux nombres, choisissez le premier"))
    range2 = int(input("vous devez choisir entre deux nombres, choisissez le second"))
    return random.randint(range1, range2)


playing = True
while playing:
    number_range = choosing_number()
    winning = False
    number_try = 0
    while not winning:
        number_try += 1

        gess_numbers = int(input(" choisissez un nombre entre les nombres que vous avez chosis"))

        if gess_numbers > number_range:
            print("votre nombre est trop grand, choisissez un plus petit")
        elif gess_numbers < number_range:
            print("votre nombre est trop petit, choisissez un plus grand")
        else:
            print("Vous avez fini en:", number_try)
            winning = True

    recommencer = input("est ce que vous voulez recommencez y/n")
    if recommencer == "n":
        playing = False
