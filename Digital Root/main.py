def digital_root(n):
    while n >= 10:
        list1 = []
        list1[:0] = str(n)
        sum_my = 0
        for x in list1:
            sum_my += int(x)
        n = sum_my
    return n

