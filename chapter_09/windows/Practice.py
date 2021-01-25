def is_product_availability_matrix(matrix_a, matrix_b):  # fin
    return len(matrix_a[0]) == len(matrix_b)


def matrix_product(matrix_a, matrix_b):
    if not is_product_availability_matrix(matrix_a, matrix_b):
        raise ArithmeticError
    return [[sum(a*b for a, b in zip(row_a, column_b))
            for column_b in zip(*matrix_b)]
            for row_a in matrix_a]


matrix_x = [[2, 5], [1, 1]]
matrix_y = [[1, 1, 2], [2, 1, 1]]
matrix_z = [[2, 4], [5, 3], [1, 3]]

print(matrix_product(matrix_y, matrix_z))
# Expected value: [[9, 13], [10, 14]]
print(matrix_product(matrix_z, matrix_x))
# Expected value: [[8, 14], [13, 28], [5, 8]]
print(matrix_product(matrix_x, matrix_x))
# Expected value: [[9, 15], [3, 6]]
print(matrix_product(matrix_z, matrix_w))
# Expected value: False
