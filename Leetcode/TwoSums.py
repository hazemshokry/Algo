def twosum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return [i,j]

def twosum_v2(nums, target):
    d = {}
    for i in range(len(nums)):
        val = target - nums[i]
        if val in d:
            return [d[val], i]
        else:
            d[nums[i]] = i

if __name__ == '__main__':
    print(twosum_v2([2, 7, 11, 15],9))
    print(twosum([2, 7, 11, 15],9))