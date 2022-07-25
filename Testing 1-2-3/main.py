def number(lines):
    new_list = []
    counter = 1
    for x in lines:
        new_list.append(f'{counter}: {x}')
        counter += 1
    return new_list