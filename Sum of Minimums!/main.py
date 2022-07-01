def sum_of_minimums(numbers):
    suma = 0
    for x in numbers:
        suma += min(x)
    return suma