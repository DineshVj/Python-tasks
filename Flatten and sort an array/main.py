def flatten_and_sort(array):
    lista = []
    for table in array:
        if len(table)>0:
            for x in table:
                lista.append(x)
    lista.sort()
    return lista