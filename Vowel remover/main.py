def shortcut( s ):
    lista = ['a', 'e', 'i', 'o', 'u']
    for char in s:
        if char in lista:
            s = s.replace(char, '')
    return s