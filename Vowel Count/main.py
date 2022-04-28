def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = 0
    for char in sentence:
        if char in vowels:
            counter +=1
    return counter