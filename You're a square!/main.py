def is_square(n):
    if n>=0:
        return (n**0.5).is_integer()
    else:
        return False