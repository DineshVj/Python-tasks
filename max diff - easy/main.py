def max_diff(lst):
    if len(lst)>1:
        mini = min(lst)
        maxi = max(lst)
        return abs(mini-maxi)
    else:
        return 0