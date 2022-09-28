def same_case(a, b): 
    if a.isalpha() == 0 or b.isalpha() == 0:
        return -1
    elif a.islower() and b.islower():
        return 1
    elif a.isupper() and b.isupper():
        return 1
    else:
        return 0
