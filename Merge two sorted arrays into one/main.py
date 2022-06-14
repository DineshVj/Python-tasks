def merge_arrays(arr1, arr2):
    arr_3 = arr1 +arr2
    arr_3 = list(set(arr_3))
    arr_3.sort()
    return arr_3