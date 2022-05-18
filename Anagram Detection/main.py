# write the function is_anagram
def is_anagram(test, original):
    test = list(test.lower())
    test.sort()
    original = list(original.lower())
    original.sort()
    if test == original:
        return True
    else:
        return False
