def bumps(road):
    counter = 0
    for x in road:
        if x == 'n':
            counter += 1
    if counter > 15:
        return 'Car Dead'
    else:
        return 'Woohoo!'