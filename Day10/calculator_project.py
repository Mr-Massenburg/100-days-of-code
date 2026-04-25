# Day 10 | Calculator Project - Functions with outputs

from art import logo
from os import system

def add(n1, n2):
    """Takes two numbers and adds them together"""
    return n1 + n2

def subtract(n1, n2):
    """Takes two numbers and subtracts the second number from the first number"""
    return n1 - n2

def multiply(n1, n2):
    """Takes two numbers and multiplies them together"""
    return n1 * n2

def divide(n1, n2):
    """Takes two numbers divides the first number by the second number"""
    return n1 / n2

math_functions = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}
fresh_calc = True

while fresh_calc:
    print(logo)

    keep_result = True

    num1 = float(input("What's the first number?: "))

    while keep_result:

        for symbol in math_functions:
            print(symbol)

        operation = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))

        result = math_functions[operation](num1, num2)

        print(f"{num1} {operation} {num2} = {result}")

        another_calc = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start a new calculation: ")

        if another_calc == 'y':
            num1 = result
        else:
            keep_result = False
            system("clear")  # macOS / Linux
            # system("cls")  # Windows | I use macOS so I have commented this clear out
