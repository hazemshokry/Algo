def helper_compare(a, b):
    if abs(a) < abs(b):
        return True
    elif abs(a) > abs(b):
        return False
    elif abs(a) == abs(b):
        if a < b:
            return True
        elif a > b:
            return False


def absSort(arr):
    arr_length = len(arr)
    for i in range(arr_length):
        for j in range(i + 1, arr_length):
            if helper_compare(arr[j], arr[i]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr

def absSort_v2(arr):
    return sorted(arr, key=lambda x: abs(x))

###
if __name__ == '__main__':
    arr = [2, -7, -2, -2, 0]
    print(absSort(arr))
    print(absSort_v2(arr))

    d = {"a": 4, "c": 2, "b": 3}
    x = sorted(d.values())
    print(d.items())