# A left rotation operation on an array shifts each of the array's elements 1 unit to the left.
# For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2].

def rotLeft(a, d):
    for rot in range(d):
        for i in range(len(a) - 1):
            a[i], a[i + 1] = a[i + 1], a[i]

    return a


def rotLeft_v2(a, d):
    res = []
    res = a[d:] + a[:d]
    return res


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    print(rotLeft(a, 2))
    #print(rotLeft_v2(a, 4))
