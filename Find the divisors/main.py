def divisors(integer):
    new_list = []
    for f in range(2,integer):
        if (integer % f) == 0:
            new_list.append(f)
    if len(new_list) > 0:
        return new_list
    else:
        return f"{integer} is prime"