def printer_error(s):
    counter = 0
    for x in s:
        if ord(x)>109:
            counter+=1
    return f'{counter}/{len(s)}'