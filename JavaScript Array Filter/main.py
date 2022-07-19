def get_even_numbers(arr):
    even = filter(lambda p: p%2 == 0, arr)
    return list(even)