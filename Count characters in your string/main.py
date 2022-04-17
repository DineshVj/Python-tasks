def count(string):
    my_dict = {}
    my_list = list(string)
    for x in my_list:
        counter = my_list.count(x)
        my_dict[x] = counter
    return my_dict