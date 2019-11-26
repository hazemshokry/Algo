def maxSubArray(nums):
    max = -99999999999
    for i in range(len(nums)):
        runningWindowSum = 0
        for j in range(i, len(nums)):
            runningWindowSum = runningWindowSum + nums[j]
            if runningWindowSum > max:
                max = runningWindowSum
    return max

if __name__ == '__main__':
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))