from functools import reduce


def vector_size_check(*vector_variables):  # fin
    return len(set([len(vector) for vector in vector_variables])) == 1


def vector_addition(*vector_variables):  # fin
    return [sum(t) for t in zip(*vector_variables)]\
        if vector_size_check(*vector_variables) else 'ArithmeticError'


def vector_subtraction(*vector_variables):  # fin
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    return [reduce(lambda x, y: x-y, t) for t in zip(*vector_variables)]


def scalar_vector_product(alpha, vector_variable):  # fin
    return [alpha*t for t in vector_variable]


def matrix_size_check(*matrix_variables):  # fin
    return len(set([len(matrix) for matrix in matrix_variables])) == 1


def is_matrix_equal(*matrix_variables):  # fin
    result = True
    for matrix in zip(*matrix_variables):
        for t in zip(*matrix):
            if not len(set(t)) == 1:
                result = False
    return result


def matrix_addition(*matrix_variables):  # fin
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return [[sum(t) for t in zip(*matrix)]
            for matrix in zip(*matrix_variables)]


def matrix_subtraction(*matrix_variables):  # fin
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return [[reduce(lambda x, y: x-y, t) for t in zip(*matrix)]
            for matrix in zip(*matrix_variables)]


def matrix_transpose(matrix_variable):  # fin
    return [[*matrix] for matrix in zip(*matrix_variable)]


def scalar_matrix_product(alpha, matrix_variable):  # fin
    return [[alpha*t for t in matrix] for matrix in matrix_variable]


def is_product_availability_matrix(matrix_a, matrix_b):  # fin
    return len(matrix_a[0]) == len(matrix_b)


def matrix_product(matrix_a, matrix_b):
    if not is_product_availability_matrix(matrix_a, matrix_b):
        raise ArithmeticError
    return [[sum(a*b for a, b in zip(row_a, column_b))
            for column_b in zip(*matrix_b)]
            for row_a in matrix_a]
