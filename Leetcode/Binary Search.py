# Given a sorted (in ascending order) integer array nums of n elements and a target value,
# write a function to search target in nums. If target exists, then return its index, otherwise return -1

def binary_search(nums, target):

    if not nums:
        return -1

    left, right = 0, len(nums) - 1

    while left <= right:
        mid_index = int(left + (right - left) / 2)
        if nums[mid_index] == target:
            return mid_index
        elif nums[mid_index] > target:
            right= mid_index - 1
        elif nums[mid_index] < target:
            left = mid_index + 1

    return  -1

if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    print(binary_search(nums, 12))