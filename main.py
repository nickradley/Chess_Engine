#DeezNutzInc Chess Engine
from tkinter import *

#generic comment
#generic comment 2
#generic comment 3

WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1200
SQUARESIZE = 100
BOARD_HORIZ_OFFSET = 100
BOARD_VERT_OFFSET = 20

def init_window():
    window=Tk()
    window.title('Chess Engine')
    window.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
    window.configure(bg="grey")
    canvas = Canvas(window, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
    for file in range(8):
        for rank in range(8):
            square = canvas.create_rectangle(BOARD_HORIZ_OFFSET + (SQUARESIZE * rank),
                                             BOARD_VERT_OFFSET + (SQUARESIZE * file),
                                             BOARD_HORIZ_OFFSET + (SQUARESIZE * (rank + 1)),
                                             BOARD_VERT_OFFSET + (SQUARESIZE * (file + 1)),
                                             fill='black' if (file + rank) % 2 != 0 else 'white')
    canvas.place(anchor= "nw")


    lbl=Label(window, text="Press the button below me", bg='black', fg='gray', font=("Helvetica", 16))
    lbl.place(x=950, y=100)
    btn=Button(window, text="You are Retarded", bg='black', fg='black')
    btn.place(x=950, y=150)
    window.mainloop()


init_window()