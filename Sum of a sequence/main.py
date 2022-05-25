def sequence_sum(begin_number, end_number, step):
    counter = 0
    for x in range(begin_number, end_number +1, step):
        counter +=x
    return counter
