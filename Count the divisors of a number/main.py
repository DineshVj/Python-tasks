def divisors(n):
    counter = 0
    for x in range(1,n+1):
        if n%x == 0:
            counter += 1
    return counter