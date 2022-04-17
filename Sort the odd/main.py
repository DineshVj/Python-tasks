def sort_array(source_array):
    new_list = []
    for x in source_array:
        if x%2 == 1:
            new_list.append(x)
    new_list.sort()
    counter = 0
    for y in range(0, len(source_array)):
        if source_array[y]%2 == 1:
            source_array[y] = new_list[counter]
            counter += 1
    print(new_list)
    print(source_array)
    return source_array