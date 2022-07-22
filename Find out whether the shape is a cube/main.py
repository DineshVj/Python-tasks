def cube_checker(volume, side):
    if volume > 0 and side > 0:
        if side ** 3 == volume:
            return True
        else:
            return False
    else:
        return False