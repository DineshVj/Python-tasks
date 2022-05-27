def find_needle(haystack):
    for x in haystack:
        if x == 'needle':
            c = haystack.index(x)
            return f'found the needle at position {c}'