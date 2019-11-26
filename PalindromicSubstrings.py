def countSubstrings(s):
    dict = {x: s.count(x) for x in s}
    return dict

if __name__ == '__main__':
    print(countSubstrings("Haazem"))

