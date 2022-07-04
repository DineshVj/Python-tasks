def no_odds(values):
    new_list = []
    for x in values:
        if x % 2 == 0:
            new_list.append(x)
    return new_list