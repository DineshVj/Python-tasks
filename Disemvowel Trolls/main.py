def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for char in string_:
        if char in vowels:
            string_ = string_.replace(char, '')
    print(string_)
    return string_
