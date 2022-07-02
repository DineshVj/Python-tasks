import math
def factorial(n):
    if n>12 or n<0:
        raise ValueError("Sorry, no numbers below zero")
    else:
        return math.factorial(n)