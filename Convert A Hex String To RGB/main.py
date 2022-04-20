def hex_string_to_RGB(hex_string):
    new_dict = {}
    new_dict['r'] = int(f"{hex_string[1:3]}", 16)
    new_dict['g'] = int(f"{hex_string[3:5]}", 16)
    new_dict['b'] = int(f"{hex_string[5:7]}", 16)
    return new_dict