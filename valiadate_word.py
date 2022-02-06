def valiadate_word(word):
    res = True
    word = word.lower()
    wordcount = word.count(word[0])

    for x in word:
        if wordcount != word.count(x):
            res = False
            break
    return res
