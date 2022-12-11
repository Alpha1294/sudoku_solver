board = [
    [0, 0, 6, 0, 0, 0, 7, 8, 0],
    [0, 0, 0, 0, 0, 2, 0, 9, 0],
    [5, 0, 3, 0, 0, 8, 0, 6, 0],
    [8, 4, 0, 0, 6, 5, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 0, 5, 0],
    [7, 9, 0, 3, 2, 4, 8, 0, 0],
    [0, 5, 0, 2, 8, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 6, 7, 0, 0, 3, 0, 0, 8]
]


def solve(bo):
    # best case of recursion
    find = find_empy(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            # if they are valid we add into the board
            bo[row][col] = i

            # recursively try to find the solution
            if solve(bo):
                return True
            # if we cant find the solution with the actual value,reset it to try another value
            bo[row][col] = 0
    return False


def valid(bo, num, pos):
    # check row ,we check each element in the row ,if the position we are checking is something we insert data in,we wont bother checking that
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            # everytime we are on the third row we print a horizontal line
            print("- - - - - - - - - - - - - ")
        # bo[0] means the length of each row
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            # we check if we are at the last position
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empy(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row,col

    return None


print_board(board)
solve(board)
print("______________________________")
print_board(board)
