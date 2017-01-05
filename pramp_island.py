def count_islands(matrix):
    """In a 2D matrix with 0's and 1's, count the number of islands (1's). A
    group of islands has 1's in adjacent cells.

        >>> count_islands([[0, 1, 0, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 1, 0], [0, 1, 1, 0, 0], [1, 0, 1, 0, 1]])
        6

    """

    island = 0

    if matrix is None or len(matrix) == 0:
        return 0

    row = len(matrix)
    col = len(matrix[0])

    def mark_island(i, j):

        islands = []
        islands.append([i, j])

        while islands:
            x, y = islands.pop()
            if matrix[x][y] == 1:
                matrix[x][y] = 2
                if x - 1 >= 0:
                    islands.append([x - 1, y])
                if x + 1 < row:
                    islands.append([x + 1, y])
                if y - 1 >= 0:
                    islands.append([x, y - 1])
                if y + 1 < col:
                    islands.append([x, y + 1])

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                mark_island(i, j)
                island += 1

    return island
