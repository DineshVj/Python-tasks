def high_and_low(numbers):
    our_list = numbers.split(' ')
    our_list = [ int(x) for x in our_list ]
    return f'{max(our_list)} {min(our_list)}'
