def most_likely(word_data):
    _max = 0
    best = None
    for next_word in word_data.keys():
        if word_data[next_word] > _max:
            best = next_word
            _max = word_data[next_word]
    return best


def chose_randomly(word_data, sentence):
    proba_table = []
    _sum = 0
    for word in word_data.keys():
        hundred = ceil(word_data[word] * 100)
        _sum = _sum + hundred
        proba_table.append((word, _sum))
    rand = randint(0, _sum)
    for i in proba_table:
        if i[1] >= rand:
            return i[0]
