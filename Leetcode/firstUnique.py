def firstUniqChar(s):
    dict = {}
    result = -1
    for i in s:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1

    for idx, i in enumerate(s):
        if dict[i] == 1:
            result = idx
            break
    return result

if __name__ == '__main__':
    print(firstUniqChar("loveleetcode"))

