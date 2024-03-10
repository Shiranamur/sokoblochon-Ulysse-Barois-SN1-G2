from functions import *
from carte import *


def main():
    while True:
        for level_index, original_level in enumerate(levels):
            print(f"Starting Level {level_index + 1}")

            level = [list(row) for row in original_level]

            while True:
                p_pos = p_tile_pos(level)
                v_tiles = v_tile_pos(level)

                level_completed = False
                while not level_completed:
                    for line in level:
                        print(" ".join(line))
                    direction = input("Move (Z=up, S=down, Q=left, D=right), R to retry, X to quit, H for help: ").lower()

                    if direction not in ["z", "s", "q", "d", "x", "h", "r"]:
                        print("Invalid input. Use Z, S, Q, D to move, R to retry, X to quit, and H for help.")
                        continue
                    elif direction == "h":
                        print("player is P, crates are C, victory points are V, Walls are X.")
                        continue
                    elif direction == "x":
                        print("Exiting the game, thank you for playing!")
                        exit(0)
                    elif direction == "r":
                        print("Restarting the level...")
                        level = [list(row) for row in original_level]
                        break

                    p_pos = apply_move(level, p_pos, v_tiles, direction)
                    c_tiles = c_tile_pos(level)

                    if sorted(c_tiles) == sorted(v_tiles):
                        for line in level:
                            print(" ".join(line))
                        print("Level Finished.")
                        level_completed = True

                if level_completed and level_index == len(levels) - 1:
                    choice = input("Congrats, you finished the game! Press R to restart or X to quit: ").lower()
                    if choice == "x":
                        print("Thank you for playing!")
                        return
                    elif choice == "r":
                        print("Restarting the game from Level 1...")
                        break
                elif level_completed:
                    break


if __name__ == "__main__":
    main()
