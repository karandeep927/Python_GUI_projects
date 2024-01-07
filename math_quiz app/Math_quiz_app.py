import random as r
from time import strftime
from tkinter import *
from tkinter import messagebox

Q_TXT = ("Verdana",12,"bold")
TXT_FONT = ("Verdana",35,"bold")
BG = "#F4B8FF"
FG = "#7343C0"
FGA = "#2b2b2a"
BGA = "#F4B8FF"
B_BG = "#D5E8F2"




def gen_question():
    num1 = r.randint(1,100)
    num2 = r.randint(1,100)
    operator = r.choice(["+","-","*"])
    return num1,num2,operator

def check_result(num1,num2,operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    return result

def main():
    frame1 = Frame(root,width=400,height=460,bg=BG)
    frame1.grid(row=0,column=0)
    frame1.propagate(0)
    welcome = Label(frame1,text="Welcome To\nMath Quiz",font=TXT_FONT,bg=BG,fg=FG).pack(pady=100,)
    start = Button(frame1,text="Start",command=question_screen,font=Q_TXT,bg=B_BG,fg=FG).pack()

def check(opt,result):
    if opt == result:
        messagebox.showinfo("Math quiz","Your answer is right")
        question_screen()
    else:
        messagebox.showinfo("Math quiz",f"wrong answer !!! :( \n Right answer is {result} ")
        question_screen()

def question_screen():
    var = IntVar()

    frame = Frame(root,width=400,height=460,bg=BG)
    frame.grid(row=0,column=0)
    frame.propagate(0)
    
    btn1 = Button(frame,text="Close",command=exit_quiz,font=Q_TXT,bg=B_BG,fg=FG)
    btn1.pack(pady=(30,0),side=TOP,padx=(320,0))
    
    logo = Label(frame,text="Math Quiz",font=TXT_FONT,bg=BG,fg=FG)
    logo.pack(pady=(10,30))
    num1,num2,operator = gen_question()
    question = f"Q. What is the answer of this problem\n     {num1} {operator} {num2} = ?"
    
    question_label = Label(frame,text=question,fg="#7343C0",bg=BG,font=("Verdana",13,"bold"),justify=LEFT)
    question_label.pack(anchor=W)

    opt1,opt2,opt3,opt4 = gen_options(num1,num2,operator)

    r1 = Radiobutton(frame,text=opt1,value=opt1,fg="#7343C0",variable=var,justify=LEFT,bg=BG,activebackground=BGA,activeforeground=FGA,font=("arial",12,"bold"))
    r1.pack(anchor=W,padx=20,pady=10) 
    r2 = Radiobutton(frame,text=opt2,value=opt2,fg="#7343C0",variable=var,justify=LEFT,bg=BG,activebackground=BGA,activeforeground=FGA,font=("arial",12,"bold"))
    r2.pack(anchor=W,padx=20,pady=10) 
    r3 = Radiobutton(frame,text=opt3,value=opt3,fg="#7343C0",variable=var,justify=LEFT,bg=BG,activebackground=BGA,activeforeground=FGA,font=("arial",12,"bold"))
    r3.pack(anchor=W,padx=20,pady=10) 
    r4 = Radiobutton(frame,text=opt4,value=opt4,fg="#7343C0",variable=var,justify=LEFT,bg=BG,activebackground=BGA,activeforeground=FGA,font=("arial",12,"bold"))
    r4.pack(anchor=W,padx=20,pady=10) 

    result = check_result(num1,num2,operator)
    btn2 = Button(frame,text="check",command=lambda:check(var.get(),result),font=("Verdana",12,"bold"),bg=B_BG,fg=FG,pady=10).pack(pady=(10))

def gen_options(num1,num2,operator):
    option = [r.randrange(1,500,8) for i in range(3)]
    r_option = check_result(num1,num2,operator)
    option.insert(r.randint(0,4),r_option)
    return option

def exit_quiz():
    choice = messagebox.askyesno("Math Quiz","Do you want to Quit the Quiz :( ")
    if choice:
        main()

root = Tk()
root.title("Math Quiz")
root.resizable(0,0)
main()
root.mainloop()
