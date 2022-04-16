def create_phone_number(n):
    final_string = '('
    for x in range(0, 3):
        final_string += str(n[x])
    final_string += ') '
    for x in range(3, 6):
        final_string += str(n[x])
    final_string += '-'
    for x in range(6, 10):
        final_string += str(n[x])
    return final_string