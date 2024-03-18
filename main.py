from random import randint as randint

T_PLATEAU:int = 3
HUMAIN:str = 'X'
ORDI:str = 'O'

# exo1

def init_plateau():
    """
    NoneType -> list(list(str))
    Retourne le plateau initial du jeu.
    """
    return [[' ' for i in range(3)] for j in range(3)]

# exo2

def print_plateau(plateau:list):
    """
    list(list) -> NoneType
    :param (plateau): Un plateau sous la forme d'une liste de listes.
    Affiche un plateau sous la forme usuelle du tic-tac-toe.
    """
    ligne_plateau:str = ""
    ligne:str = ""
    for i in range(len(plateau)):
        for j in range(len(plateau[0])):
            ligne_plateau += plateau[i][j]
            if j != len(plateau[i]) - 1:
                ligne_plateau += '|'
                ligne += '--'
        print(ligne_plateau)
        if i != len(plateau) - 1:
            print(ligne + '-')
        ligne = ""
        ligne_plateau = ""
    print('')

# exo3

def input_humain(plateau):
    """
    list(list) -> tuple(int, int)
    :param (plateau): Un plateau sous la forme d'une liste de listes.
    Demande le coup de l'utilisateur (coordonnées où il veut placer le symbole), puis retourne un couple contenant les coordonnées choisies.
    """
    x:str = ''
    y:str = ''
    while len(x) != 1 or not(ord('1') <= ord(x) <= ord(str(T_PLATEAU))) or not(int(x) > 0) or len(y) != 1 or not(ord('1') <= ord(y) <= ord(str(T_PLATEAU))) or not(int(y) > 0) or plateau[int(y)-1][int(x)-1] != ' ':
        x = input("Entrez le numéro de la colonne où vous voulez votre symbole.")
        y = input("Entrez le numéro de la ligne où vous voulez votre symbole.")
    return (int(x)-1, int(y)-1)

# exo4

def coords_vides(plateau):
    """
    list(list) -> list(tuple(int, int))
    :param (plateau): Un plateau de tic-tac-toe sous forme de liste de listes.
    Retourne une liste contenant tous les couples de coordonnées dont leur position est vide.
    """
    liste_coords:list = []
    for i in range(len(plateau)):
        for j in range(len(plateau[0])):
            if plateau[i][j] == ' ':
                liste_coords.append((j, i))
    return liste_coords

# exo5

def input_ordi(plateau):
    """
    list(list) -> tuple(int, int)
    :param (plateau): Un plateau de tic-tac-toe sous forme de liste de listes.
    Tire au hasard une des positions vides du plateau et retourne un couple de coordonnées constituant le coup de l'ordinateur.
    """
    liste_pos_vides:list = coords_vides(plateau)
    return liste_pos_vides[randint(0, len(liste_pos_vides) - 1)]

# exo6

def est_victoire(symbole:str, plateau:list):
    """
    str, list(list) -> bool
    :param (symbole, plateau): Symbole du joueur humain ou ordinateur ; Un plateau de tic-tac-toe sous forme de liste de listes.
    Retourne True si le joueur passé en paramètre a gagné (aligné 3 de ses symboles), sinon retourne False.
    """
    if plateau[0][1] == symbole:
        if (plateau[0][0] == symbole and plateau[0][2] == symbole) or (plateau[1][1] == symbole and plateau[2][1] == symbole):
            return True
    
    elif plateau[1][1] == symbole:
        if (plateau[0][0] == symbole and plateau[2][2] == symbole) or (plateau[0][2] == symbole and plateau[2][0] == symbole) or (plateau[1][0] == symbole and plateau[1][2] == symbole):
            return True
    
    elif plateau[2][1] == symbole and (plateau[2][0] == symbole and plateau[2][2] == symbole):
        return True
    
    elif plateau[1][0] == symbole and (plateau[0][0] == symbole and plateau[2][0] == symbole):
        return True
    
    elif plateau[1][2] == symbole and (plateau[0][2] == symbole and plateau[2][2] == symbole):
        return True
    
    return False

# exo7

def joue_partie():
    """
    NoneType -> NoneType
    Permet de lancer une partie de jeu tic-tac-toe.
    """
    plateau:list = init_plateau()
    coup_humain:tuple = ()
    coup_ordi:tuple = ()
    print_plateau(plateau)
    while ' ' in [plateau[i][j] for i in range(len(plateau)) for j in range(len(plateau[i]))]:
        coup_humain = input_humain(plateau)
        plateau[coup_humain[1]][coup_humain[0]] = HUMAIN
        print_plateau(plateau)
        if est_victoire(HUMAIN, plateau):
            print("Félicitation ! Vous avez gagné la partie !")
            return
        if coords_vides(plateau) == []:
            return
        coup_ordi = input_ordi(plateau)
        plateau[coup_ordi[1]][coup_ordi[0]] = ORDI
        print_plateau(plateau)
        if est_victoire(ORDI, plateau):
            print("L'ordinateur a gagné. Le joueur n'est pas très fort :)")
            return

# exo8

def input_rejouer():
    """
    NoneType -> bool
    Retourne True si l'utilisateur a décidé de jouer une nouvelle partie, sinon retourne False.
    """
    return input("Voulez-vous jouer une nouvelle partie ? (y/n)") == 'y'

# exo9

def main():
    """
    NoneType -> NoneType
    Jeu du tic-tac-toe.
    """
    joue_partie()
    while input_rejouer():
        joue_partie()
    
if __name__ == '__main__':
    main()