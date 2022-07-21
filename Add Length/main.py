def add_length(str_):
    lista = str_.split(' ')
    lista_2 = []
    for x in lista:
        lista_2.append(f'{x} {len(x)}')
    return lista_2