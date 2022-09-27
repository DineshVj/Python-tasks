def close_compare(a, b, margin=0):
    if margin == 0:
        return a - b
    else:
        if a + margin < b:
            return -1
        elif a > b + margin:
            return 1
        else:
            return 0
