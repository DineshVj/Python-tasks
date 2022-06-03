def correct(s):
    for char in s:
        if char == '5':
            s = s.replace(char, 'S')
        if char == '0':
            s = s.replace(char, 'O')
        if char == '1':
            s = s.replace(char, 'I')
            print(s)
    print(s)
    return s