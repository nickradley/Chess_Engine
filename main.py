#DeezNutzInc Chess Engine
from tkinter import *

#generic comment

window=Tk()
window.title('Chess Engine')
window.geometry('500x500+500+400')
window.configure(bg='black')
lbl=Label(window, text="Press the button below me", bg='black', fg='gray', font=("Helvetica", 16))
lbl.place(x=170, y=180)
btn=Button(window, text="You are Retarded", bg='black', fg='blue')
btn.place(x=200, y=200)
window.mainloop()


