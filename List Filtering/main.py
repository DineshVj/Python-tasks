def filter_list(l):
    new_list = []
    for e in l:
        if not isinstance(e, str):
            new_list.append(e)
    return new_list