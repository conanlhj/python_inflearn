vector_a = [1, 2, 10]  # List로 표현했을 경우
vector_b = (1, 2, 10)  # Tuple로 표현했을 경우
vector_c = {'x': 1, 'y': 2, 'z': 10}  # Dict로 표현했을 경우

print(vector_a, vector_b, vector_c)

u = [2, 2]
v = [2, 3]
z = [3, 5]
result = []
for i in zip(u, v, z):
    result.append(sum(i))
print(result)

result = [sum(t) for t in zip(u, v, z)]
print(result)

u = [1, 2, 3]
v = [4, 5, 6]
alpha = 2

result = [alpha*sum(t) for t in zip(u, v)]
print(result)

matrix_a = [[3, 6], [4, 5]]  # List로 표현했을 경우
matrix_b = [(3, 6), (4, 5)]  # Tuple로 표현했을 경우
matrix_c = {(0, 0): 3, (0, 1): 6, (1, 0): 4, (1, 1): 5}  # Dict로 표현했을 경우

matrix_a = [[3, 6], [4, 5]]
matrix_b = [[5, 8], [6, 7]]
result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]
print(result)

alpha = 4
result = [[alpha * element for element in t] for t in matrix_a]
print(result)

matrix_a = [[1, 2, 3], [4, 5, 6]]
result = [[element for element in t] for t in zip(*matrix_a)]
print(result)

matrix_a = [[1, 1, 2], [2, 1, 1]]
matrix_b = [[1, 1], [2, 1], [1, 3]]
result = [[sum(a*b for a, b in zip(row_a, column_b))
          for column_b in zip(*matrix_b)] for row_a in matrix_a]
print(result)


def vector_addition(*args):
    return [sum(t) for t in zip(*args)]


print(vector_addition([1, 2], [2, 3], [3, 4]))
