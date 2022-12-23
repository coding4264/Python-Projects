from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.title("Tic-Tac-Toe")

bclick = True
buttons = StringVar()



def winner(buttons):
    if(button1[Text] == "O" and button2[Text] == "O" and button3[Text] == "O" or
       button4[Text] == "O" and button5[Text] == "O" and button6[Text] == "O" or
       button7[Text] == "O" and button8[Text] == "O" and button9[Text] == "O" or
       button1[Text] == "O" and button4[Text] == "O" and button7[Text] == "O" or
       button2[Text] == "O" and button5[Text] == "O" and button8[Text] == "O" or
       button3[Text] == "O" and button6[Text] == "O" and button9[Text] == "O" or
       button1[Text] == "O" and button5[Text] == "O" and button9[Text] == "O" or
       button3[Text] == "O" and button5[Text] == "O" and button7[Text] == "O"):
       messagebox.showinfo("Player O Wins")
    elif(button1[Text] == "X" and button2[Text] == "X" and button3[Text] == "X" or
       button4[Text] == "X" and button5[Text] == "X" and button6[Text] == "X" or
       button7[Text] == "X" and button8[Text] == "X" and button9[Text] == "X" or
       button1[Text] == "X" and button4[Text] == "X" and button7[Text] == "X" or
       button2[Text] == "X" and button5[Text] == "X" and button8[Text] == "X" or
       button3[Text] == "X" and button6[Text] == "X" and button9[Text] == "X" or
       button1[Text] == "X" and button5[Text] == "X" and button9[Text] == "X" or
       button3[Text] == "X" and button5[Text] == "X" and button7[Text] == "X"):
       messagebox.showinfo("PLayer X Wins")


def buttonClick(button):
    global bclick
    if buttons[Text] == " " and bclick == True:
        buttons[Text] = "X"
        bclick = False
    elif buttons[Text] == " " and bclick == False:
        buttons[Text] = "O"
        bclick = True
    winner(buttons)
button1 = Button(tk, text = ' ',command=lambda:buttonClick(button1))
button1.grid(row = 1,column=0,sticky= S+N+E+W)

button2 = Button(tk, text = ' ',command=lambda:buttonClick(button2))
button2.grid(row = 1,column=1,sticky= S+N+E+W)

button3 = Button(tk, text = ' ',command=lambda:buttonClick(button3))
button3.grid(row = 1,column=2,sticky= S+N+E+W)

button4 = Button(tk, text = ' ',command=lambda:buttonClick(button4))
button4.grid(row = 2,column=0,sticky= S+N+E+W)

button5 = Button(tk, text = ' ',command=lambda:buttonClick(button5))
button5.grid(row = 2,column=1,sticky= S+N+E+W)

button6 = Button(tk, text = ' ',command=lambda:buttonClick(button6))
button6.grid(row = 2,column=2,sticky= S+N+E+W)

button7 = Button(tk, text = ' ',command=lambda:buttonClick(button7))
button7.grid(row = 3,column=0,sticky= S+N+E+W)

button8 = Button(tk, text = ' ',command=lambda:buttonClick(button8))
button8.grid(row = 3,column=1,sticky= S+N+E+W)

button9 = Button(tk, text = ' ',command=lambda:buttonClick(button9))
button9.grid(row = 3,column=2,sticky= S+N+E+W)

tk.mainloop()