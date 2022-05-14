def square_digits(num):
    string = str(num)
    final_str = ''
    for char in string:
        final_str += str(int(char)**2)
    return int(final_str)