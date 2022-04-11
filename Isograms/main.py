def is_isogram(string):
    mylist = []
    new_list = []
    flag = True
    string_1 = string.lower()
    new_list[:0] = string_1
    print(new_list)
    mylist = list(dict.fromkeys(new_list))
    print(mylist)
    if len(new_list) <= len(mylist):
        flag = True
    else:
        flag = False
    return flag