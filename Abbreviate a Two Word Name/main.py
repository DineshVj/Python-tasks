def abbrev_name(name):
    name = name.upper()
    our_list = name.split(' ')
    return f'{our_list[0][0]}.{our_list[1][0]}'