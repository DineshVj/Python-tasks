def row_weights(array):
    nowa = [0,0]
    for x in range(len(array)):
        if x % 2 == 0:
            nowa[0] += array[x]
        else:
            nowa[1] += array[x]
    return tuple(nowa)