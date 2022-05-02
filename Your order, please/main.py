def order(sentence):
    our_dict = {}
    final_string = ''
    my_list = sentence.split(' ')
    for x in my_list:
        for char in x:
            if char.isdigit():
                our_dict[int(char)] = x
    array = sorted(our_dict.keys())
    for number in array:
        final_string += our_dict[number] + ' '
    final_string = final_string.strip()
    return final_string