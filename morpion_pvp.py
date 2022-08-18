# Programme d'un morpion Player VS Player (pas de bot)

def annonce():
    print("Voici le morpion et ceci est le plateau de jeux :")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")


def morpion_pvp():
    annonce()
    # Création du plateau qui enregistre les positions
    plateau = [" " for _ in range(9)]
    compteur = 0
    partie_en_cours = True

    def affichage():
        print(plateau[0], "|", plateau[1], "|", plateau[2])
        print("--+---+--")
        print(plateau[3], "|", plateau[4], "|", plateau[5])
        print("--+---+--")
        print(plateau[6], "|", plateau[7], "|", plateau[8])

    while partie_en_cours == True:
        position = int(input("Choisis un chiffre entre 1 et 9 : "))
        position = position - 1  # Une liste commence par 0, 1, 2, ...
        compteur = compteur + 1
        if plateau[position] != " ":
            print("ERROR >> Case déjà prise")
            # Annule le tour et la ligne suivante lance la nouvelle itération
            compteur = compteur - 1
            continue
        else:
            if compteur % 2 == 0:  # vérifie si le compteur de tour est paire ou impair pour attribuer des O ou des X
                plateau[position] = "O"
            else:
                plateau[position] = "X"

        affichage()

    # Impossible de créer une fonction rules et d'y inclure break pour stoper la partie une fois remportée
        if plateau[0] == plateau[1] == plateau[2] != " " \
                or plateau[3] == plateau[4] == plateau[5] != " "\
                or plateau[6] == plateau[7] == plateau[8] != " "\
                or plateau[0] == plateau[3] == plateau[6] != " "\
                or plateau[1] == plateau[4] == plateau[7] != " "\
                or plateau[2] == plateau[5] == plateau[8] != " "\
                or plateau[0] == plateau[4] == plateau[8] != " "\
                or plateau[6] == plateau[4] == plateau[2] != " ":
            print("Bravo, les {0} gagnent !" .format(plateau[position]))
            play_again()
            break

        elif compteur == 9:
            print("Egalité !")
            play_again()
            break

        else:
            partie_en_cours = True


def play_again():
    play = input("Voulez vous rejouer ? (Y/N)")
    if play == "y" or play == "Y" or play == "YES" or play == "yes" or play == "Yes":
        morpion_pvp()
    else:
        exit


morpion_pvp()
