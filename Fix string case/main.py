def solve(s):
    count_b = 0
    count_s = 0
    for x in s:
        if x.islower():
            count_s += 1
        else:
            count_b += 1
    if count_s >= count_b:
        return s.lower()
    else:
        return s.upper()