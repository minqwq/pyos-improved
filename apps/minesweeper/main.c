/*
 * StarHikari Studios 2022~2024
 * 
 * sys/game
 * Minesweeper v1.1
 *
 * Compatible with Windows and *nix
 *
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 10

typedef enum {
    COVERED,
    FLAGGED,
    REVEALED
} CellState;

typedef struct {
    int hasMine;
    int adjacentMines;
    CellState state;
} Cell;

Cell board[SIZE][SIZE];

void initializeBoard() {
    // Random Seed
    srand(time(NULL));

    // Initialize the board
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            board[i][j].hasMine = 0;
            board[i][j].adjacentMines = 0;
            board[i][j].state = COVERED;
        }
    }

    // Place mines randomly
    for (int i = 0; i < 10; i++) {
        int x, y;
        do {
            x = rand() % SIZE;
            y = rand() % SIZE;
        } while (board[x][y].hasMine);

        board[x][y].hasMine = 1;

        // Update adjacent mine counts
        for (int dx = -1; dx <= 1; dx++) {
            for (int dy = -1; dy <= 1; dy++) {
                int nx = x + dx;
                int ny = y + dy;
                if (nx >= 0 && nx < SIZE && ny >= 0 && ny < SIZE && !board[nx][ny].hasMine) {
                    board[nx][ny].adjacentMines++;
                }
            }
        }
    }
}

/*
void printBoard() {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j].state == REVEALED) {
                if (board[i][j].hasMine) {
                    printf("M ");
                } else {
                    printf("%d ", board[i][j].adjacentMines);
                }
            } else if (board[i][j].state == FLAGGED) {
                printf("F ");
            } else {
                printf(". ");
            }
        }
        printf("\n");
    }
}
*/

void printBoard() {
    printf("  ");
    for (int j = 0; j < SIZE; j++) {
        printf("%d ", j);
    }
    printf("\n");

    for (int i = 0; i < SIZE; i++) {
        printf("%d ", i);
        for (int j = 0; j < SIZE; j++) {
            if (board[i][j].state == REVEALED) {
                if (board[i][j].hasMine) {
                    printf("M ");
                } else {
                    printf("%d ", board[i][j].adjacentMines);
                }
            } else if (board[i][j].state == FLAGGED) {
                printf("F ");
            } else {
                printf(". ");
            }
        }
        printf("\n");
    }
}


void revealCell(int x, int y) {
    if (x < 0 || x >= SIZE || y < 0 || y >= SIZE || board[x][y].state != COVERED) {
        return;
    }

    board[x][y].state = REVEALED;
    if (board[x][y].hasMine) {
        printf("Game Over! You hit a mine.\n");
        exit(0);
    } else if (board[x][y].adjacentMines == 0) {
        for (int dx = -1; dx <= 1; dx++) {
            for (int dy = -1; dy <= 1; dy++) {
                revealCell(x + dx, y + dy);
            }
        }
    }
}

// Function for flagging mines
void flagCell(int x, int y) {
    if (x < 0 || x >= SIZE || y < 0 || y >= SIZE || board[x][y].state == REVEALED) {
        return;
    }

    if (board[x][y].state == COVERED) {
        board[x][y].state = FLAGGED;
    } else if (board[x][y].state == FLAGGED) {
        board[x][y].state = COVERED;
    }
}

void clearScreen() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

int main() {
    initializeBoard();
    char command;
    int x, y;

    while (1) {
        clearScreen();
        printBoard();
        printf("(o x y to open, f x y to flag, q to quit)\nInput Command: ");
        scanf(" %c", &command);

        if (command == 'q') {
            break;
        }

        scanf("%d %d", &x, &y);

        if (command == 'o') {
            revealCell(x, y);
        } else if (command == 'f') {
            flagCell(x, y);
        } else {
            printf("Invalid command.\n");
        }
    }

    printf("Exiting game.\n");
    return 0;
}
