def string_clean(s):
    final = ''
    for x in s:
        if not x.isnumeric():
            final += x
    return final