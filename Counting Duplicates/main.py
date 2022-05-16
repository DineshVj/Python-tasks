def duplicate_count(text):
    text = text.lower()
    print(text)
    counter = 0
    new_list = []
    for x in text:
        if text.count(x) >1 and x not in new_list:
            counter +=1
            new_list.append(x)
    return counter