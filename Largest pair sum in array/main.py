def largest_pair_sum(numbers): 
    e1 = max(numbers)
    numbers.remove(max(numbers))
    e2 = max(numbers)
    return e1 + e2