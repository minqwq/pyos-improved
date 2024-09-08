import random
import os

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('  1 2 3')
    for i, row in enumerate(board):
        print(f'{i + 1} {" ".join(row)}')

def check_winner(board, player):
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for condition in win_conditions:
        if all(board[x][y] == player for x, y in condition):
            return True
    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def player_move(board):
    while True:
        try:
            move = input("(x y)=move, q=quit, c=restart: ").strip().lower()
            if move == 'q':
                return 'q'
            if move == 'c':
                return 'c'
            x, y = map(int, move.split())
            x, y = x - 1, y - 1
            if board[x][y] == ' ':
                board[x][y] = 'X'
                break
            else:
                print("Cell is already taken.")
        except (ValueError, IndexError):
            print("Invalid input.")

def computer_move(board):
    empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    x, y = random.choice(empty_positions)
    board[x][y] = 'O'
    print(f"Computer select {x + 1} {y + 1}")

def main():
    while True:
        board = initialize_board()
        print_board(board)
        while True:
            result = player_move(board)
            if result == 'q':
                print("Quit.")
                return
            if result == 'c':
                break
            print_board(board)
            if check_winner(board, 'X'):
                print("Player win!")
                break
            if is_full(board):
                print("Tic!")
                break

            computer_move(board)
            print_board(board)
            if check_winner(board, 'O'):
                print("Computer win!")
                break
            if is_full(board):
                print("Tic!")
                break

if __name__ == "__main__":
    main()
