def remove_consecutive_duplicates_6(s):
    results = []
    string = s.split()
    for word in range(len(string)):
        if word not in results:
            results.append(word)
        else:
            results[-1] != word
            results.append(word)
    return ' '.join(results)
