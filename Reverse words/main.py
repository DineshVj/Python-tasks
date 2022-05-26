def reverse_words(text):
    final_list = []
    text_list = text.split(' ')
    for element in text_list:
        final_list.append(element[::-1])
    return ' '.join(final_list)
