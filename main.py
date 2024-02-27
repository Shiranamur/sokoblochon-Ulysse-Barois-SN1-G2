from functions import *
from carte import *

def main():

    level = map

    player_pos = player_init_pos(level)

    while True:
        for line in level:
            print(" ".join(line))

        direction = input("Move (Z=up, S=down, Q=left, D=right), Press X to quit or H to get some help: ")

        if direction not in ["z", "s", "q", "d", "x", "h"]:
            print("Invalid input. Please use z, s, q, d for movement, x to quit and h for help")
            continue
        elif direction == "x":
            print("Exiting the game, thank you for playing !")
            break
        elif direction == "h":
            print("git gud bro")
            continue

        new_player_pos = move_check(level, player_pos, direction, object_move)

        if new_player_pos != player_pos:
            level[player_pos[0]][player_pos[1]] = " "
            level[new_player_pos[0]][new_player_pos[1]] = "I"
            player_pos = new_player_pos

        victory_tiles = victory_tile_pos(level)
        crates_on_tiles = crate_tile_pos(level)
        if sorted(victory_tiles) == sorted(crates_on_tiles):
            print("Congratulations! You've won!")
            break


if __name__ == "__main__":
    main()


