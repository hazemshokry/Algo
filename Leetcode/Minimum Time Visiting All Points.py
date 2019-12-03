# On a plane there are n points with integer coordinates points[i] = [xi, yi].
# Your task is to find the minimum time in seconds to visit all points.
# You can move according to the next rules:
# In one second always you can either move vertically, horizontally by one unit or diagonally
# (it means to move one unit vertically and one unit horizontally in one second).
# You have to visit the points in the same order as they appear in the array.
# Input: points = [[1,1],[3,4],[-1,0]]
# Output: 7
# Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]

def minTimeToVisitAllPoints(points):
    """
    1 1
    3 4
    -1 0
    :param points:
    :return:
    """
    length_points = len(points)
    total_cost = 0
    for p in range(length_points-1):
        x1 = points[p][0]
        x2 = points[p+1][0]
        y1 = points[p][1]
        y2 = points[p+1][1]
        total_cost += get_cost(x1,y1, x2, y2)

    return total_cost

def get_cost(x1, y1, x2, y2):
    if x1 == x2:
        return abs(y2 - y1)
    elif y1 == y2:
        return abs(x2 - x1)
    else:
        return max((abs(x2 - x1), abs(y1 - y2)))

if __name__ == '__main__':
    print(minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
