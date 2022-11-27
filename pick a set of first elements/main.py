def first(seq, n = 1):
    if n > len(seq):
        return seq
    elif n == 0:
        return []
    else:
        return seq[:n]
