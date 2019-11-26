def missingNumber(nums) -> int:
    nums = sorted(nums)
    if len(nums) == 1 and nums[0] == 1:
        return 0
    elif len(nums) == 1 and nums[0] == 0:
        return 1
    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] != 1:
            return nums[i + 1] - 1
    return 1

if __name__ == '__main__':
    print (missingNumber([9,6,4,2,3,5,7,0,1]))
