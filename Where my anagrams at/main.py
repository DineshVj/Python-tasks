def anagrams(word, words):
    word_list = list(word)
    new_dict = {}
    check_dict = {}
    final_list = []
    for k in word_list:
        new_dict[k] = word_list.count(k)

    for word in words:
        words_list = list(word)
        for char in words_list:
            check_dict[char] = words_list.count(char)
        if check_dict == new_dict:
            final_list.append(word)
        check_dict = {}
    return final_list