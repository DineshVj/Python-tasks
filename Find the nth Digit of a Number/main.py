def find_digit(num, nth):
    number = str(abs(num))
    if nth <= 0:
        return -1
    elif nth>len(number):
        return 0
    else:
        return int(number[-nth])