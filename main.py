import random

playing = True
while playing:
    range1 =int(input("vous devez choisir entre deux nombres, choisissez le premier"))
    range2 =int(input("vous devez choisir entre deux nombres, choisissez le second"))
    pc_number = random.randint(range1,range2)
    winning = False
    number_try = 0
    while not winning:

        number_try += 1

        try:
            gess = int(input(" choisissez un nombre entre 1 et 1000"))
        except ValueError:
            print(" vous devez choisir un nombre seulement! ")

        if gess > pc_number:
            print("votre nombre est trop grand, choisissez un plus petit")
        elif gess < pc_number:
            print("votre nombre est trop petit, choisissez un plus grand")
        else:
            print("Vous avez fini en:", number_try)
            winning = True

    recommencer = input("est ce que vous voulez recommencez y/n")
    if recommencer == "n":
        playing = False


