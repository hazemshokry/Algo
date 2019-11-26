def CheckPermutation(string1, string2):
    string1sorted = ''.join(sorted(string1))
    string2sorted = ''.join(sorted(string2))
    if string1sorted in string2sorted:
        return True
    elif string2sorted in string1sorted:
        return True
    return False

if __name__ == '__main__':
    print(CheckPermutation("ab", "eidbaooo"))
    print(CheckPermutation("ab", "eidboaoo"))
