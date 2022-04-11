def friend(x):
    new_list = []
    for element in x:
        if len(element) == 4:
            new_list.append(element)
    return new_list