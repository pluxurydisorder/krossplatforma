def print_board(board):
    print(" ".join(["." if x == 0 else "S" if x == 1 else "G" for x in board]))


def instructions():
    print("IN THIS GAME YOU ARE GIVEN 8 BALLS ON A 9 HOLE")
    print("BOARD. THE OBJECT IS TO REVERSE THE ORDER OF THE BALLS")
    print("THE 'S' ARE SILVER BALLS AND THE 'G' ARE GOLD.")
    print("YOU MUST SET THE SILVER TO WHERE THE GOLD ARE AND")
    print("THE GOLD TO WHERE THE SILVER ARE. THE SPACE IS")
    print("A PERIOD ON THE BOARD.")
    print("GOOD LUCK!! HERE IS THE BOARD:")
    print()


def main():
    print(" " * 22 + "JUMPING BALLS")
    print(" " * 20 + "CREATIVE COMPUTING")
    print(" " * 18 + "MORRISTOWN, NEW JERSEY")
    print("\n" * 3)

    # Initial game board
    board = [1, 1, 1, 1, 0, 2, 2, 2, 2]
    moves = 0

    instructions()
    while True:
        print_board(board)
        moves += 1

        # Get user input
        try:
            move_from = int(input("MOVE FROM (1-9): ")) - 1
            move_to = int(input("MOVE TO (1-9): ")) - 1
        except ValueError:
            print("INVALID INPUT. TRY AGAIN.")
            continue

        # Validate input
        if not (0 <= move_from < 9 and 0 <= move_to < 9):
            print("ILLEGAL MOVE. POSITIONS MUST BE BETWEEN 1 AND 9.")
            continue

        # Check move validity
        if abs(move_from - move_to) == 1 or abs(move_from - move_to) == 2:
            if board[move_from] != 0 and board[move_to] == 0:
                board[move_to] = board[move_from]
                board[move_from] = 0
            else:
                print(f"ILLEGAL MOVE. POSITION {move_to + 1} IS OCCUPIED OR NO BALL AT {move_from + 1}.")
                continue
        else:
            print("ILLEGAL MOVE. BALLS CAN ONLY MOVE TO ADJACENT OR JUMP OVER ONE POSITION.")
            continue

        # Check win condition
        if board[:4] == [2, 2, 2, 2] and board[5:] == [1, 1, 1, 1]:
            print_board(board)
            print(f"YOU WIN!!! YOU COMPLETED THE GAME IN {moves} MOVES!!!!")
            play_again = input("PLAY AGAIN? (Y/N): ").strip().upper()
            if play_again == "Y":
                board = [1, 1, 1, 1, 0, 2, 2, 2, 2]
                moves = 0
                continue
            else:
                print("THANKS FOR PLAYING!")
                break


if __name__ == "__main__":
    main()