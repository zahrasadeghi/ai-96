def find_word_repeats(words_array):
    result = {}
    for word in words_array:
        if word in result.keys():
            result[word] += 1
        else:
            result[word] = 1
    return result
