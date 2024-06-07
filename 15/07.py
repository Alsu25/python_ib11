heightsMap = [[1, 2, 3, 4],
              [100, 50, 6, 200],
              [7, 0, 0, 0]]


def find_mountain(heightsMap):
    return max((heightsMap[i][j], (i, j)) for i in range(len(heightsMap)) for j in range(len(heightsMap[0])))[1]


print(find_mountain(heightsMap))