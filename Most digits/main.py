def find_longest(arr):
    length = len(str((max(arr))))
    for number in arr:
        if len(str(number)) == length:
            return number