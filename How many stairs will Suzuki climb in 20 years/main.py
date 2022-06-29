def stairs_in_20(stairs):
    suma = 0
    for table in stairs:
        suma += sum(table)
    return suma*20