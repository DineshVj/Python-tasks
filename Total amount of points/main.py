def points(games):
    suma = 0
    for x in games:
        if x[0]>x[-1]:
            suma +=3
        if x[0]==x[-1]:
            suma +=1
    return suma