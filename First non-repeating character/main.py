def first_non_repeating_letter(string):
    my_list = list(string.lower())
    big_list = list(string)
    new_list = []
    for k in my_list:
        if my_list.count(k) > 1:
            pass
        else:
            new_list.append(my_list.index(k))
    if len(new_list) > 0:
        return big_list[new_list[0]]
    else:
        return ''


