# Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.
# Example :
# Input:
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
import sys


def numMatchingSubseq(S, words):
    count = 0
    for w in words:
        if checkSubseq(S, w):
            count += 1
    return count

def checkSubseq(S, word):
    """
    This should be solved by indexing or BS
    abcde
        f
    cw
     s
    """
    fast,slow = 0,0

    while fast < len(S) and slow < len(word):
        if S[fast] == word[slow]:
            slow += 1
        fast += 1

    if slow == len(word):
        return True
    else:
        return False

if __name__ == '__main__':
    print(numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))
