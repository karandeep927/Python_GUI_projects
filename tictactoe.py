from tkinter import *

from tkinter import messagebox


HG = 2

WD = 5

count = 0

current_player = "X"


root = Tk()

root.title("Tic Tac Toe")

root.resizable(False,False)

def check_win():
    """
    This function check wether the X Win or O Win the Game and ask the user to restart the Game
    """
    
    win_message =  'Win the game :) \n Do you want to restart the Game'

    if (btn1["text"] == btn2["text"] == btn3["text"]) and (btn1["text"] != " " and btn2["text"] != " " and btn3["text"] != " "):

        btn1.config(bg="red",fg="white")

        btn2.config(bg="red",fg="white")

        btn3.config(bg="red",fg="white")

        response = messagebox.askyesno("Tic Tac Toe",f"{btn1['text']} {win_message}")
        if response:
            play()
        else:
            root.destroy()
    

    elif (btn4["text"] == btn5["text"] == btn6["text"]) and (btn4["text"] != " " and btn5["text"] != " " and btn6["text"] != " "):

        btn4.config(bg="red",fg="white")

        btn5.config(bg="red",fg="white")

        btn6.config(bg="red",fg="white")

        response = messagebox.askyesno("Tic Tac Toe",f"{btn4['text']} {win_message}")
        if response:
            play()
        else:
            root.destroy()


    elif (btn7["text"] == btn8["text"] == btn9["text"]) and (btn7["text"] != " " and btn8["text"] != " " and btn9["text"] != " ") :

        btn7.config(bg="red",fg="white")

        btn8.config(bg="red",fg="white")

        btn9.config(bg="red",fg="white")

        response = messagebox.askyesno("Tic Tac Toe",f"{btn7['text']} {win_message}")
        if response:
            play()
        else:
            root.destroy()


    elif (btn1["text"] == btn4["text"] == btn7["text"]) and (btn1["text"] != " " and btn4["text"] != " " and btn7["text"] != " "):

        btn1.config(bg="red",fg="white")

        btn7.config(bg="red",fg="white")

        btn4.config(bg="red",fg="white")

        response = messagebox.askyesno("Tic Tac Toe",f"{btn1['text']} {win_message}")
        if response:
            play()
        else:
            root.destroy()
    

    elif (btn3["text"] == btn6["text"] == btn9["text"]) and (btn3["text"] != " " and btn6["text"] != " " and btn9["text"] != " "):

        btn3.config(bg="red",fg="white")

        btn6.config(bg="red",fg="white")

        btn9.config(bg="red",fg="white")

        response = messagebox.askyesno("Tic Tac Toe",f"{btn3['text']} {win_message}")
        if response:
            play()
        else:
            root.destroy()


    elif (btn2["text"] == btn5["text"] == btn8["text"]) and (btn2["text"] != " " and btn5["text"] != " " and btn8["text"] != " ") :

        btn2.config(bg="red",fg="white")

        btn5.config(bg="red",fg="white")

        btn8.config(bg="red",fg="white")

        response = messagebox.askyesno("Tic Tac Toe",f"{btn2['text']} {win_message}")
        if response:
            play()
        else:
            root.destroy()
    

    elif (btn1["text"] == btn5["text"] == btn9["text"]) and (btn1["text"] != " " and btn5["text"] != " " and btn9["text"] != " "):

        btn1.config(bg="red",fg="white")

        btn5.config(bg="red",fg="white")

        btn9.config(bg="red",fg="white")

        response = messagebox.askyesno("Tic Tac Toe",f"{btn1['text']} {win_message}")
        if response:
            play()
        else:
            root.destroy()

    elif (btn3["text"] == btn5["text"] == btn7["text"]) and (btn3["text"] != " " and btn5["text"] != " " and btn7["text"] != " "):

        btn3.config(bg="red",fg="white")

        btn7.config(bg="red",fg="white")

        btn5.config(bg="red",fg="white")

        response = messagebox.askyesno("Tic Tac Toe",f"{btn3['text']} {win_message}")
        if response:
            play()
        else:
            root.destroy()

    elif count == 9:

        response = messagebox.askyesno("Tic Tac Toe",f"It's Draw :( \n Try again.....")
        if response:
            play()
        else:
            root.destroy()


def change_btn_value(value,btn):
    """
    This function take the current_player and button as arguments and configure the button and 
    fill the value into button text 
    """
    global count,current_player

    btn["text"] = value

    btn['state'] = DISABLED

    count += 1

    check_win()

    if current_player == "X":

        current_player = "O"

    else:
        current_player = "X"


def play():

    global btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,count
    count=0

    btn1 = Button(root,text=" ",bg="pink",font="arial 30",command=lambda :change_btn_value(current_player,btn1),width=WD,height=HG)

    btn1.grid(row=0,column=0)

    btn2 = Button(root,text=" ",bg="pink",font="arial 30",command=lambda :change_btn_value(current_player,btn2),width=WD,height=HG)

    btn2.grid(row=0,column=1)

    btn3 = Button(root,text=" ",bg="pink",font="arial 30",command=lambda :change_btn_value(current_player,btn3),width=WD,height=HG)

    btn3.grid(row=0,column=2)

    btn4 = Button(root,text=" ",bg="pink",font="arial 30",command=lambda :change_btn_value(current_player,btn4),width=WD,height=HG)

    btn4.grid(row=1,column=0)

    btn5 = Button(root,text=" ",bg="pink",font="arial 30",command=lambda :change_btn_value(current_player,btn5),width=WD,height=HG)

    btn5.grid(row=1,column=1)

    btn6 = Button(root,text=" ",bg="pink",font="arial 30",command=lambda :change_btn_value(current_player,btn6),width=WD,height=HG)

    btn6.grid(row=1,column=2)

    btn7 = Button(root,text=" ",bg="pink",font="arial 30",command=lambda :change_btn_value(current_player,btn7),width=WD,height=HG)

    btn7.grid(row=2,column=0)

    btn8 = Button(root,text=" ",bg="pink",font="arial 30",command=lambda :change_btn_value(current_player,btn8),width=WD,height=HG)

    btn8.grid(row=2,column=1)

    btn9 = Button(root,text=" ",bg="pink",font="arial 30",command=lambda :change_btn_value(current_player,btn9),width=WD,height=HG)

    btn9.grid(row=2,column=2)

if __name__ == "__main__":
    play()

root.mainloop()



