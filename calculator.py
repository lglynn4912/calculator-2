"""CLI application for a prefix-notation calculator."""

from xml.etree.ElementTree import TreeBuilder
from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
def tokenize_input():
    user_input = input('> ')
    tokens = user_input.split(" ")

    while True:
        if tokens == "+":
            