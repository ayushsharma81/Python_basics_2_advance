def minSumPathRec(triangle, i, j):

    #  Base case: no value below the last row,
    #  return 0
    if i == len(triangle):
        return 0

    # find the min path sum from 
    # current cell till the last row
    return triangle[i][j] + min(minSumPathRec(triangle, i+1, j),
                                minSumPathRec(triangle, i+1, j+1))


def minSumPath(triangle):
    return minSumPathRec(triangle, 0, 0)

if __name__ == "__main__":
    triangle = [
        [2],
        [3, 9],
        [1, 6, 7]
    ]
    
    print(minSumPath(triangle))
