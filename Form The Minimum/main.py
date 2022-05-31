def min_value(digits):
    digits = list(set(digits))
    digits.sort()
    stri = ''
    for el in digits:
        stri += str(el)
    return int(stri)
