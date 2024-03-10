# Récupère la position joueur
def p_tile_pos(level):
    for i, row in enumerate(level):
        for j, col in enumerate(row):
            if col == "P":
                p_pos = (i, j) # Scan la matrice et retourne un tuple
                return p_pos

#Récupère la position des tuiles de victoire
def v_tile_pos(level):
    v_tiles = []
    for i, row in enumerate(level):
        for j, col in enumerate(row):
            if col == "V":
                v_tiles.append((i, j)) # Scan la matrice et retourne un ou plusieurs tuples
    return v_tiles

#Récupère la position des caisses
def c_tile_pos(level):
    c_tiles = []
    for i, row in enumerate(level):
        for j, col in enumerate(row):
            if col == "C":
                c_tiles.append((i, j)) # Scan la matrice et retourne un ou plusieurs tuples
    return c_tiles

# Récupère l'input du joueur et calcul le contenu de la tuile suivante en fonction de la direction
def player_next_tile_check(direction, p_pos, level):
    delta = {"z": (-1, 0), "s": (1, 0), "q": (0, -1), "d": (0, 1)} # Indique la valeur à ajouter à la position en fonction de l'input
    next_p_tile = (p_pos[0] + delta[direction][0], p_pos[1] + delta[direction][1]) # additionne les valeurs du delta au tuple de la position joueur et stock dans variable.
    content_at_next_p_tile = level[next_p_tile[0]][next_p_tile[1]] # regarde le contenu de la position retourné dans la variable précédente
    if content_at_next_p_tile == " ":
        return 1
    elif content_at_next_p_tile == "X":
        return 2
    elif content_at_next_p_tile == "C":
        next_c_tile = (next_p_tile[0] + delta[direction][0], next_p_tile[1] + delta[direction][1]) # si la nouvelle tuile contient une caisse, calcul la nouvelle position de la caisse
        content_at_next_c_tile = level[next_c_tile[0]][next_c_tile[1]]
        if content_at_next_c_tile not in ["X", "C"]:
            return 3, next_c_tile
        else:
            return 4

# Logique de déplacement, need refactor
def apply_move(level, p_pos, v_tiles, direction):
    delta = {"z": (-1, 0), "s": (1, 0), "q": (0, -1), "d": (0, 1)}
    r = player_next_tile_check(direction, p_pos, level)
    if isinstance(r, tuple): #si r est un tuple
        next_c_tile = r[1] #récupère la valeur de next-c-tile
        level[next_c_tile[0]][next_c_tile[1]] = "C" # affiche un C au nouvelle emplacement de la caisse
        next_p_pos = (p_pos[0] + delta[direction][0], p_pos[1] + delta[direction][1])  # Yikes the first
        level[next_p_pos[0]][next_p_pos[1]] = "P" # affiche un P au nouvel emplacement joueur
        level[p_pos[0]][p_pos[1]] = "V" if p_pos in v_tiles else " " #affiche un v si la position joueur est dans une tuile de victoire, sinon affiche un espace
        p_pos = next_p_pos # retourne la nouvelle position joueur en tant que position joueur
        return p_pos
    else:
        if r == 1:
            next_p_pos = (p_pos[0] + delta[direction][0], p_pos[1] + delta[direction][1])  # Yikes Junior
            level[next_p_pos[0]][next_p_pos[1]] = "P"
            level[p_pos[0]][p_pos[1]] = "V" if p_pos in v_tiles else " "
            p_pos = next_p_pos
            return p_pos
        elif r == 2:
            print("there's a wall")
            return p_pos
        elif r == 4:
            print("there's something blocking you")
            return p_pos
