geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    new_list = []
    for i in birds:
        if i not in geese:
            new_list.append(i)
    return new_list