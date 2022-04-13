def to_jaden_case(string):
    new_list = []
    e = ' '
    our_list = list(string.split(' '))
    for element in our_list:
        new_list.append(element.capitalize())
    print(new_list)
    print(e.join(new_list))
    return e.join(new_list)
