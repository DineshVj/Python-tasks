def powers_of_two(n):
    final_list = []
    for x in range(0,n+1):
        final_list.append(2**x)
    return final_list