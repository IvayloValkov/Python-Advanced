rows, cols = [int(el) for el in input().split()]


def init_matrix():
    matrix = []
    for _ in range(rows):
        matrix.append(input().split())
    return matrix

def check_if_equal(r, c, matr):
    current_element = matr[r][c]
    next_element_same_row = matr[r][c+1]
    element_bottom = matr[r+1][c]
    element_bottom_right = matr[r+1][c+1]
    if current_element == next_element_same_row and next_element_same_row == element_bottom and element_bottom==element_bottom_right:
        return True
    return False


matrix = init_matrix()

counter = 0
for row_index in range(rows-1):
    for col_index in range(cols-1):
        if check_if_equal(row_index, col_index, matrix):
            counter += 1

print(counter)