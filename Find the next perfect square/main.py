import math
def find_next_square(sq):
    if sq ** (1/2) == math.floor(sq ** (1/2)):
        return (sq ** (1/2)+1)**2
    return -1
