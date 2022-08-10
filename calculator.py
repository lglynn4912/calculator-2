"""CLI application for a prefix-notation calculator."""

from xml.etree.ElementTree import TreeBuilder
from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
def tokenize_input():
    
    
    while True:
        user_input = input('> ')
        
        tokens = user_input.split(" ")
        
        token1 = int(tokens[1])
        token2 = int(tokens[2])

        # if len(tokens) < 3:
        #     token2 = "0"

        # else:
        #     token2 = tokens[2]

        if tokens[0] == "q":
            break
        elif tokens[0] == "+":
            print(add(token1, token2))
            
        elif tokens[0] == "-":
            print(subtract(token1, token2))
            
        elif tokens[0] == "*":
            print(multiply(token1, token2))
            
        elif tokens[0] == "/":
            print(divide(token1, token2))
            
        elif tokens[0] == "square":
            if len(tokens) < 3:
                tokens.append("0")
            print(square(token1))
            
        elif tokens[0] == "cube":
            print(cube(token1))
            
        elif tokens[0] == "pow":
            print(power(token1, token2))
            
        elif tokens[0] == "mod":
            print(mod(token1, token2))
            
        else:
            print("Not valid!")

tokenize_input()     