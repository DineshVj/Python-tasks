def sum_digits(number):
    counter = 0
    our_list = list(str(abs(number)))
    for el in our_list:
        counter += int(el)
    return counter