# https://oj.masaischool.com/contest/11933/problems

#def solve(N,M,matrix):
    
    # Function to print the spiral traversal of a matrix
def spiral_traversal(matrix, rows, cols):
    top_row = 0
    bottom_row = rows - 1
    left_col = 0
    right_col = cols - 1

    result = []

    while top_row <= bottom_row and left_col <= right_col:
        # Traverse top row
        for i in range(left_col, right_col + 1):
            result.append(matrix[top_row][i])
        top_row += 1

        # Traverse right column
        for i in range(top_row, bottom_row + 1):
            result.append(matrix[i][right_col])
        right_col -= 1

        # Traverse bottom row
        if top_row <= bottom_row:
            for i in range(right_col, left_col - 1, -1):
                result.append(matrix[bottom_row][i])
            bottom_row -= 1

        # Traverse left column
        if left_col <= right_col:
            for i in range(bottom_row, top_row - 1, -1):
                result.append(matrix[i][left_col])
            left_col += 1

    print(*result)

