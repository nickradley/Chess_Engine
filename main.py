# DeezNutzInc Chess Engine
from tkinter import *
from PIL import Image, ImageTk

import pathlib
import sys

WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1200
SQUARESIZE = 90
BOARD_HORIZ_OFFSET = 100
BOARD_VERT_OFFSET = 20


# the following function places pieces on the board according to a passed FEN string. For now, we consider
# only the part of the FEN which gives the location of the pieces, without considering castling rights,
# en passant, move number etc.
def FEN_to_array(FEN):
    fen_ranks = FEN.split("/")
    board = [[0] * 8 for _ in range(8)]
    row = 0
    col = 0
    for rank in fen_ranks:
        for element in rank:
            if element.isdigit():
                col += int(element)
            else:
                board[row][col] = element
                col += 1
        row += 1
        col = 0
    return board


# The following function initializes the window and places pieces based on the inputted
# fen string param
def init_window(window, canvas, fen):
    window.title('Chess Engine')
    window.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
    window.configure(bg="grey")
    canvas.pack()
    # generate board grid
    for file in range(8):
        for rank in range(8):
            x1 = BOARD_HORIZ_OFFSET + (SQUARESIZE * rank)
            y1 = BOARD_VERT_OFFSET + (SQUARESIZE * file)
            x2 = BOARD_HORIZ_OFFSET + (SQUARESIZE * (rank + 1))
            y2 = BOARD_VERT_OFFSET + (SQUARESIZE * (file + 1))
            square = canvas.create_rectangle(x1, y1, x2, y2,
                                             fill='#302311' if (file + rank) % 2 != 0 else '#cfaf86')
    # import pieces
    global black_pawn
    global black_bishop
    global black_knight
    global black_rook
    global black_king
    global black_queen
    global white_pawn
    global white_bishop
    global white_knight
    global white_rook
    global white_king
    global white_queen
    black_pawn = ImageTk.PhotoImage(Image.open("images/Black_Pawn.png"))
    black_bishop = ImageTk.PhotoImage(Image.open("images/Black_Bishop.png"))
    black_knight = ImageTk.PhotoImage(Image.open("images/Black_Knight.png"))
    black_rook = ImageTk.PhotoImage(Image.open("images/Black_Rook.png"))
    black_king = ImageTk.PhotoImage(Image.open("images/Black_King.png"))
    black_queen = ImageTk.PhotoImage(Image.open("images/Black_Queen.png"))
    white_pawn = ImageTk.PhotoImage(Image.open("images/White_Pawn.png"))
    white_bishop = ImageTk.PhotoImage(Image.open("images/White_Bishop.png"))
    white_knight = ImageTk.PhotoImage(Image.open("images/White_Knight.png"))
    white_rook = ImageTk.PhotoImage(Image.open("images/White_Rook.png"))
    white_king = ImageTk.PhotoImage(Image.open("images/White_King.png"))
    white_queen = ImageTk.PhotoImage(Image.open("images/White_Queen.png"))
    # arrange pieces according to fen param
    board = FEN_to_array(fen)
    switcher = {
        "p": black_pawn,
        "b": black_bishop,
        "n": black_knight,
        "r": black_rook,
        "k": black_king,
        "q": black_queen,
        "P": white_pawn,
        "B": white_bishop,
        "N": white_knight,
        "R": white_rook,
        "K": white_king,
        "Q": white_queen
    }
    for file in range(8):
        for rank in range(8):
            if board[file][rank] != 0:
                canvas.create_image(BOARD_HORIZ_OFFSET + (SQUARESIZE * rank) + SQUARESIZE * .15,
                                    BOARD_VERT_OFFSET + (SQUARESIZE * file) + SQUARESIZE * .15,
                                    anchor=NW, image=switcher[board[file][rank]])


def main():
    # Fetch fen command line arg, if any
    argv = sys.argv[1:]
    if len(argv) == 0:
        fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    else:
        fen = argv[0]
    # Create and init window
    window = Tk()
    canvas = Canvas(window, height=WINDOW_HEIGHT, width=WINDOW_WIDTH, bg='lightgrey')
    init_window(window, canvas, fen)
    window.mainloop()


main()
