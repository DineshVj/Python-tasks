def is_valid_walk(walk):
    if len(walk) == 10 and (walk.count('e') == walk.count('w')) and walk.count('n') == walk.count('s'):
        return True
    else:
        return False