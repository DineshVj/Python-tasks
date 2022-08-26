def div_con(table):
    suma_i = 0
    suma_str = 0
    for x in table:
        if isinstance(x, int):
            suma_i += x
        else:
            suma_str += int(x)
    return suma_i - suma_str