def pig_it(text):
    my_list = list(text.split(' '))
    print(my_list)
    for r in range(0, len(my_list)):
        if my_list[r].isalpha():
            my_list[r] = f'{my_list[r][1:]+my_list[r][0]+"ay"}'
    return ' '.join(my_list)