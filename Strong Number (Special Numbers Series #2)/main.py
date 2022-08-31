import math

def strong_num(number):
    suma = 0
    string = str(number)
    for x in string:
        suma += math.factorial(int(x))
    if suma == number:
        return 'STRONG!!!!'
    else:
        return 'Not Strong !!'