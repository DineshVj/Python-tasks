def sum_cubes(n):
    suma = 0
    for x in range(1,n+1):
        suma += x*x*x
    return suma