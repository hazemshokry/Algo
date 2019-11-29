# Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island.
# For example, the below matrix contains 5 islands
# Input : mat[][] = {{1, 1, 0, 0, 0},
#                    {0, 1, 0, 0, 1},
#                    {1, 0, 0, 1, 1},
#                    {0, 0, 0, 0, 0},
#                    {1, 0, 1, 0, 1}

def get_islands_count(matrix):
    matrix_length_rows = len(matrix)
    matrix_length_cols = len(matrix[0])
    number_of_islands = 0
    visited = [[False for j in range(matrix_length_cols)] for i in range(matrix_length_rows)]

    for row in range(matrix_length_rows):
        for col in range(matrix_length_cols):
            if matrix[row][col] == 1 and not visited[row][col]:
                number_of_islands += 1
                check_valid_island(matrix, row, col, visited)
    return number_of_islands

def check_valid_island(matrix, row, col, visited):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return
    if matrix[row][col] == 0 or visited[row][col]:
        return
    visited[row][col] = True
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r != row or col != c:
                check_valid_island(matrix, r, c, visited)


if __name__ == '__main__':
    matrix = [     [1, 1, 0, 0, 0],
                   [0, 1, 0, 0, 1],
                   [1, 0, 0, 1, 1],
                   [0, 0, 0, 0, 0],
                   [1, 0, 1, 0, 1]]
    print(get_islands_count(matrix))
