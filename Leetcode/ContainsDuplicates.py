def containsDuplicate(nums):
    d = {}
    for num in nums:
        if num not in d:
            d[num] = 1
        else:
            return False
    return True

if __name__ == '__main__':
    print(containsDuplicate([1,1,2,3]))