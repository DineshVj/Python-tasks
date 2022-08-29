def get_number_from_string(string):
    number = ''
    for x in string:
        if x.isdigit():
            number += x
    return int(number)