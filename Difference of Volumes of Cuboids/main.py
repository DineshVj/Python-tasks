def find_difference(a, b):
    vol_a = 1
    vol_b = 1
    for el in a:
        vol_a *= el
    for el in b:
        vol_b *= el
    return abs(vol_b-vol_a)