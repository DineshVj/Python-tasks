def f(n):
    if isinstance(n, int):
        if n > 0:
            suma = 0
            for x in range(n+1):
                suma += x
            return suma
        else:
            return None