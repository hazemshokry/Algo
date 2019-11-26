

def topKFrequent(nums, k):
    if len(nums) == 0 or k == 0:
        return []

    d = {}
    result = set([])
    min = 0

    for i in nums:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1

        if min < d[i]:
            min = d[i]

        if len(result) <= k:
            result.add(min)
        else:
            result.remove(min)
            result.add(d[i])

    return result

if __name__ == '__main__':
    res = topKFrequent([1,1,1,2,2,3], 2)
    print (res)