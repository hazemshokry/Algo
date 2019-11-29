def urlify(string, len):
    res = ["%20" if c == " " else c for c in string[0:len]]
    return ''.join(res)


if __name__ == '__main__':
    print(urlify("Mr John Smith   ",13))