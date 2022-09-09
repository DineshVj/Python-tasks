def fold_to(distance):
    counter = 0
    thickness = 0.0001
    if distance >= 0:
        while distance > thickness:
            thickness *= 2
            counter += 1
        return counter
    else:
        return None