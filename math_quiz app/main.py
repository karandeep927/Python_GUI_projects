import random as r
from time import strftime

point = 0

def check_result(num1,num2,operator,user_input):
    global point
    result = None
    
    if operator == "+":
        result = num1 + num2
    if operator == "-":
        result = num1 - num2
    if operator == "*":
        result = num1 * num2
    if user_input == result:
        point += 1
        return "Your Answer is right"
    else:
        point -= 1
        return f"Your Answer is wrong \n correct Answer is {result}"

def gen_question():
    num1 = r.randint(1,100)
    num2 = r.randint(1,100)
    operator = r.choice(["+","-","*"])
    play(num1,num2,operator)

def play(num1,num2,operator):
    global point
    print("What is the answer of this problem")
    print(num1,operator,num2)
    try:
        user_input = int(input("Enter the answer: "))
        if user_input == 0:
            print("Quitting......")
            print(f"your points are {point}")
        else:
            print(check_result(num1,num2,operator,user_input))
            gen_question()
    except Exception as e:
        print("Please Enter valid number")
        play(num1,num2,operator)

if __name__ == "__main__":
    gen_question()