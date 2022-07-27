def adjacent_element_product(array):
    current = -1000000
    for x in range(len(array)-1):
        multi = array[x] * array[x+1]
        if multi >= current:
            current = multi
            print(array[x])
    return current
