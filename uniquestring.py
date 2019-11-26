def uniquestring (string):
    temp = {}
    temp = {char for char in string if any(char not in temp)}
    if len(string) != len(temp):
        return False
    else:
        return True

if __name__ == '__main__':
    string = "Hazem"
    uniquestring(string)
    print ( uniquestring(string))
