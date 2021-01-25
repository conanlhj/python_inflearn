# General
result = []
for i in range(10):
    result.append(i)
print(result)

# List comprehension
result = [i for i in range(10)]
print(result)

result = [i for i in range(10) if i % 2 == 0]
print(result)

print('\n\n')

word_1 = 'Hello'
word_2 = 'World!'
result = [i+j for i in word_1 for j in word_2]
print(result)

print('\n\n')

case_1 = ['A', 'B', 'C']
case_2 = ['D', 'E', 'A']
result = [i+j for i in case_1 for j in case_2]
print(result)
result = [i+j for i in case_1 for j in case_2 if not(i == j)]
print(result)  # if 문에서 'AA'가 빠짐

print('\n\n')

words = "The quick brown fox jumps over the lazy dog".split()
result = [[w.upper(), w.lower(), len(w)] for w in words]
print(result)

print('\n\n')

case_1 = ['A', 'B', 'C']
case_2 = ['D', 'E', 'A']
result = [i+j for i in case_1 for j in case_2]
print(result)
result = [[i+j for i in case_1] for j in case_2]
print(result)
result_2 = [element for x in result for element in x]
print(result_2)
