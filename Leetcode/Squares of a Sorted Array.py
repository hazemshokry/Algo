# Given an array of integers A sorted in non-decreasing order,
# return an array of the squares of each number, also in sorted non-decreasing order.
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

def sortedSquares(arr):
    return sorted(map((lambda i: i * i), arr))

if __name__ == '__main__':
    print(sortedSquares([-4,-1,0,3,10]))
