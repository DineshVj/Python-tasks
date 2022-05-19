def replace_exclamation(s):
    vowels = 'aeiouAEIOU'
    for char in s:
        if char in vowels:
            s = s.replace(char, '!')
    return s
