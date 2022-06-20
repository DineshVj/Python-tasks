def sum_mul(n, m):
    if n>0 and m>0:
        suma = 0
        for i in range(n,m,n):
            suma +=i
        return suma
    else:
        return 'INVALID'