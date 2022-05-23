def open_or_senior(data):
    last_list = []
    for el in data:
        if int(el[0]) >=55 and int(el[1]) > 7:
            last_list.append("Senior")
        else:
            last_list.append("Open")
    return last_list