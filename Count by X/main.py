def count_by(x, n):
    new_list = []
    for e in range(x, x*n+1):
        if e%x ==0:
            new_list.append(e)
    return new_list
