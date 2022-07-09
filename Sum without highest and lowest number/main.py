def sum_array(arr):
    if arr == None:
        return 0
    elif len(arr)>=3:
        arr.sort()
        return sum(arr[1:-1])
    else:
        return 0