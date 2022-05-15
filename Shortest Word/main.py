def find_short(s):
    es = s.split(' ')
    new_list = []
    for e in es:
        new_list.append(len(e))
    return min(new_list)