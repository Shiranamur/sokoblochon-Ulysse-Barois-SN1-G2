def player_init_pos(level):
    player_pos = None
    for i, line in enumerate(level):
        for j, section in enumerate(line):
            if section == "I":
                player_pos = (i,j)
        if player_pos:
            return player_pos

def victory_tile_pos(level):
    positions_o = []
    for i, line in enumerate(level):
        for j, section in enumerate(line):
            if section == "o":
                positions_o.append((i,j))
    return positions_o

def crate_tile_pos(level):
    positions_c = []
    for i, line in enumerate(level):
        for j, section in enumerate(line):
            if section == "<)":
                positions_c.append((i,j))
    return positions_c


def object_move(direction, player_pos):
    delta = {"z": (-1, 0), "s": (1, 0), "q": (0, -1), "d": (0, 1)}
    delta_i, delta_j = delta[direction]
    new_i = player_pos[0] + delta_i
    new_j = player_pos[1] + delta_j
    return new_i, new_j


def move_check(level, player_pos, direction, object_move):

    new_player_pos=object_move(direction, player_pos)
    current_tile_content=level[player_pos[0]][player_pos[1]]
    new_tile_content=level[new_player_pos[0]][new_player_pos[1]]

    if new_tile_content == "X":
        print("There's a wall !")
        return player_pos

    elif new_tile_content == "<)":

        push_pos = object_move(direction, new_player_pos)

        if level[push_pos[0]][push_pos[1]] == " ":
            print("You pushed a box !")
            level[new_player_pos[0]][new_player_pos[1]] = " "
            level[push_pos[0]][push_pos[1]] = "<)"
            return new_player_pos
        elif level[push_pos[0]][push_pos[1]] == "o":
            print("You pushed a box on a victory point !")
            level[new_player_pos[0]][new_player_pos[1]] = "o"
            level[push_pos[0]][push_pos[1]] = "<)"
            return new_player_pos
        else:
            print("Can't push the box !")
            return player_pos
    else:
        return new_player_pos
