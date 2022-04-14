def longest(a1, a2):
    final_string = ''
    # reading to list string 1
    list1 = []
    list1[:0] = a1

    # reading to list string 2
    list2 = []
    list2[:0] = a2

    # deleting duplicates
    list1 = list(dict.fromkeys(list1))
    list2 = list(dict.fromkeys(list2))

    # deleting elements
    for element in list1:
        for x in list2:
            if element == x:
                list2.remove(x)

    joined_list = (list1 + list2)

    joined_list.sort()

    for x in joined_list:
        final_string += x

    return final_string
