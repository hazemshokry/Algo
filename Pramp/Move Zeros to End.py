def moveZerosToEnd(arr):
    """
    @param arr: int[]
    @return: int[]

    Input: 1D array contains integers.
  Output:
    Same array but all zeros moved to the end,
  Brute Force:
    O(N^2) -> Bubble all zeroes to end
    N is array length.

    Space complexity: O(N)
    Create another empty array to save my non-zeros values
    Create another empty array to save my zeros values
    Merge them together.

  Optimal:
    O(N) return the same array, replacement in place

  Edge case:
    Values are not integers.
    Array is empty.

  Asuumption:

  Toolbox:
    2 pointers

  arr = [1, 10, 6, 4, 0, 0, 0, 0]
                      s
                                f

  """


    arr_length = len(arr)
    slow = 0
    fast = 0
    while fast < arr_length:
        if arr[fast] != 0 and arr[slow] == 0:
            arr[fast], arr[slow] = arr[slow], arr[fast]
            slow += 1

        if arr[slow] != 0:
            slow += 1

        fast += 1

    return arr

if __name__ == '__main__':
    arr = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
    print(moveZerosToEnd(arr))



