def array_diff(a, b):
    last = []
    for char in a:
        if char not in b:
            last.append(char)
    return last