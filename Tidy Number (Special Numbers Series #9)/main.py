def tidyNumber(n):
    lista = list(str(n))
    for i in range(0,len(lista)-1):
        if lista[i] <= lista[i+1]:
            pass
        else:
            return False
    return True
