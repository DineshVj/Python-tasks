def stray(arr):
    var = 0
    for el in arr:
        if arr.count(el) == 1:
            var = el
            break
    return var