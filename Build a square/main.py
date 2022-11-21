def generate_shape(n):
    lista = []
    for x in range(n):
        lista.append('+'*n)
    return '\n'.join(lista)