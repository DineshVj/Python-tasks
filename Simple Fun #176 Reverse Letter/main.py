def reverse_letter(string):
    new_string = ''
    for x in string:
        if x.isalpha():
            new_string += x
    return new_string[::-1]
