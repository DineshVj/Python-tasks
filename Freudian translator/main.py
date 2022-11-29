def to_freud(sentence):
    if sentence == '':
        return ''
    else:
        counter = sentence.count(' ') + 1
        words = ['sex' for x in range(counter)]
        return ' '.join(words)