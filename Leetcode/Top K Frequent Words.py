# Given a non-empty list of words, return the k most frequent elements.
#
# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency,
# then the word with the lower alphabetical order comes first.

# Input: ["i", "love", "Algo", "i", "love", "coding"], k = 2
# Output: ["i", "love"]

def top_k_frequent_word(arr, k):
    d = {i: arr.count(i) for i in arr}
    d = dict(sorted(d.items()))
    result = []
    for i in range(k):
        temp = ("",0)
        for j in d:
            if d[j] > temp[1] and j not in result :
                temp = (j,d[j])
        result.append(temp[0])
    return result

if __name__ == '__main__':
    arr0 = ["i", "love", "Algo", "i", "love", "coding"]
    arr1 = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]

    print(top_k_frequent_word(arr0, 3))
    print(top_k_frequent_word(arr1, 4))