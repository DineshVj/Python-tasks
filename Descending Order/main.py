def descending_order(num):
    num_s = str(num)
    num_s = sorted(num_s)
    num_s = "". join(num_s)
    return int(num_s[::-1])