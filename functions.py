def p_tile_pos(level):  # get player tile position
    for i, row in enumerate(level):
        for j, col in enumerate(row):
            if col == "P":
                p_pos = (i, j)
                return p_pos


def v_tile_pos(level):  # get victory tile position
    v_tiles = []
    for i, row in enumerate(level):
        for j, col in enumerate(row):
            if col == "V":
                v_tiles.append((i, j))
    return v_tiles


def c_tile_pos(level):  # get crate tile pos
    c_tiles = []
    for i, row in enumerate(level):
        for j, col in enumerate(row):
            if col == "C":
                c_tiles.append((i, j))
    return c_tiles


def p_next_tile(direction, p_pos, level):
    delta = {"z": (-1, 0), "s": (1, 0), "q": (0, -1), "d": (0, 1)}
    next_p_tile = (p_pos[0] + delta[direction][0], p_pos[1] + delta[direction][1])

    content_at_next_p_tile = level[next_p_tile[0]][next_p_tile[1]]

    if content_at_next_p_tile == " ":
        return 1
    elif content_at_next_p_tile == "X":
        return 2
    elif content_at_next_p_tile == "C":
        next_c_tile = (next_p_tile[0] + delta[direction][0], next_p_tile[1] + delta[direction][1])
        content_at_next_c_tile = level[next_c_tile[0]][next_c_tile[1]]
        if content_at_next_c_tile not in ["X", "C"]:
            return 3, next_c_tile
        else:
            return 4


def apply_move(level, p_pos, v_tiles, direction):
    delta = {"z": (-1, 0), "s": (1, 0), "q": (0, -1), "d": (0, 1)}
    r = p_next_tile(direction, p_pos, level)
    if isinstance(r, tuple):
        if r[0] == 3:
            next_c_tile = r[1]
            level[next_c_tile[0]][next_c_tile[1]] = "C"
            next_p_pos = (p_pos[0] + delta[direction][0], p_pos[1] + delta[direction][1])
            level[next_p_pos[0]][next_p_pos[1]] = "P"
            level[p_pos[0]][p_pos[1]] = "V" if p_pos in v_tiles else " "
            p_pos = next_p_pos
            return p_pos
    else:
        if r == 1:
            next_p_pos = (p_pos[0] + delta[direction][0], p_pos[1] + delta[direction][1])
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

