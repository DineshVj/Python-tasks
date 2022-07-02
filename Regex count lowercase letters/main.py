def lowercase_count(strng):
    counter = 0
    for x in strng:
        if x.islower():
            counter += 1
    return counter