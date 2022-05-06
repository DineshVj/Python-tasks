def find_it(seq):
    counter = 0
    for number in seq:
        counter = seq.count(number)
        if counter%2 != 0:
            return number