def move_zeros(array):
    for k in array:
        if k == 0:
            array.remove(k)
            array.append(0)
    return array