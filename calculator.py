"""CLI application for a prefix-notation calculator."""

from xml.etree.ElementTree import TreeBuilder
from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
def tokenize_input():
    
    
    while True:
        user_input = input('> ')
        
        tokens = user_input.split(" ")
        operator = (tokens[0])
        num1 = int(tokens[1])
   
        if len(tokens) < 3:
            num2 = "0"
        else:
            num2 = int(tokens[2])

        if tokens[0] == "+":
            print(add(num1,num2))
        elif tokens[0] == "-":
            print(subtract(num1,num2))
        elif tokens[0] == "*":
            print(multiply(num1,num2))
        elif tokens[0] == "/":
            print(divide(num1,num2))
        elif tokens[0] == "square":
            print(square(num1))
        elif tokens[0] == "cube":
            print(cube((num1)))
        elif tokens[0] == "pow":
            print(power(num1, num2))
        elif tokens[0] == "mod":
            print(mod(num1, num2))
            
        else:
            print("Not valid!")

tokenize_input()     