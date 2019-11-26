def wordcount (words):
    d = {}
    d = {word: 1 if word not in d else d[word] + 1 for word in words}
    return d

if __name__ == '__main__':
    print(wordcount(["Hazem", "Sayed", "Sayed", "Hazem"]))

