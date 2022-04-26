#DeezNutzInc Chess Engine
from tkinter import *
from PIL import ImageTk,Image
import pathlib

WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1200
SQUARESIZE = 90
BOARD_HORIZ_OFFSET = 100
BOARD_VERT_OFFSET = 20
#the following function places pieces on the board according to a passed FEN string. For now, we consider
# only the part of the FEN which gives the location of the pieces, without considering castling rights,
# en passant, move number etc.
def FEN_to_array(FEN):
    fen_ranks=FEN.split("/")
    board=[[0]*8for _ in range(8)]
    row=0
    col=0

    for rank in fen_ranks:
        for element in rank:
            if (element.isdigit()):
                col+=int(element)
            else:
                board[row][col]=element
                col+=1
        row+=1
        col=0
    return board

def init_window(window, canvas):
    window.title('Chess Engine')
    window.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
    window.configure(bg="grey")
    canvas.pack()
    for file in range(8):
        for rank in range(8):
            square = canvas.create_rectangle(BOARD_HORIZ_OFFSET + (SQUARESIZE * rank),
                                             BOARD_VERT_OFFSET + (SQUARESIZE * file),
                                             BOARD_HORIZ_OFFSET + (SQUARESIZE * (rank + 1)),
                                             BOARD_VERT_OFFSET + (SQUARESIZE * (file + 1)),
                                             fill='#302311' if (file + rank) % 2 != 0 else '#cfaf86')
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
    board = FEN_to_array("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
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
            if (board[rank][file] != 0):
                id=canvas.create_image(BOARD_HORIZ_OFFSET + (SQUARESIZE * rank),
                                    BOARD_VERT_OFFSET + (SQUARESIZE * file),
                                    anchor=NW, image=switcher[board[rank][file]])

window=Tk()
canvas = Canvas(window, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
init_window(window, canvas)
window.mainloop()
