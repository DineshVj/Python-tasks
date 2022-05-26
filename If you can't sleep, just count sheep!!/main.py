def count_sheep(n):
    final_string = ''
    for x in range(1,n+1):
        final_string += (f'{x} sheep...')
    return final_string