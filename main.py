from functions import *
from carte import *


def main():

    p_pos = p_tile_pos(levels)
    v_tiles = v_tile_pos(levels)
    c_tiles = c_tile_pos(levels)

    print(p_pos, c_tiles)

    while True:
        for line in levels:
            print(" ".join(line))

        if c_tiles == v_tiles:
            print("Congratulations!")
            break

        direction = input("Move (Z=up, S=down, Q=left, D=right), Press X to quit or H to get some help: ")

        if direction.lower() not in ["z", "s", "q", "d", "x", "h"]:
            print("Invalid input. Please use z, s, q, d for movement, x to quit and h for help")
        elif direction.lower() == "h":
            print("git gud bro")
        elif direction.lower() == "x":
            print("Exiting the game, thank you for playing !")
            break
        else:
            p_pos = apply_move(levels, p_pos, v_tiles, direction)
            c_tiles = c_tile_pos(levels)


if __name__ == "__main__":
    main()
