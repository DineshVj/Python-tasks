def is_triangle(a, b, c):
    new_list = [a,b,c]
    new_list.sort()
    if new_list[-1] < sum(new_list[0:2]):
        return True
    else:
        return False