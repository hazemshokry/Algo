#Given a 2D array (matrix) inputMatrix of integers,
# create a function spiralCopy that copies inputMatrix’s values into a 1D array in a spiral order,
# clockwise. Your function then should return that array. Analyze the time and space complexities of your solution.
def spiral_copy(inputMatrix):
    inputMatrix_length_row = len(inputMatrix)
    inputMatrix_length_col = len(inputMatrix[0])
    result = []

    min_row = 0
    max_col = inputMatrix_length_col - 1
    min_col = 0
    max_row = inputMatrix_length_row

    while (min_row < inputMatrix_length_row
           and min_col < inputMatrix_length_col):

        # increase cols
        for col in range(min_col, max_col):
            temp = inputMatrix[min_row][col]
            result.append(temp)

        min_row += 1

        # increasing rows
        for row in range(min_row, max_row):
            temp = inputMatrix[row][max_col]
            result.append(temp)

        max_col -= 1

        # decrease cols
        for col in range(max_col, min_col, -1):
            temp = inputMatrix[max_row][col]
            result.append(temp)

        max_row -= 1

        # decrease rows
        for row in range(max_row, min_row, -1):
            temp = inputMatrix[row][min_col]
            result.append(temp)

        min_col += 1