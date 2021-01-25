for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

print('\n\n')

mylist = ["a", "b", "c", "d"]
a = list(enumerate(mylist))
print(a)
b = {i: j for i, j in enumerate('Gachon University is an academic institute\
    located in South Korea'.split())}
print(b)

print("\n\n")

a_list = ['a1', 'a2', 'a3']
b_list = ['b1', 'b2', 'b3']
for a, b in zip(a_list, b_list):
    print(a, b)

a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c)
d = [sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))]
print(d)

print('\n\n')

a_list = ['a1', 'a2', 'a3']
b_list = ['b1', 'b2', 'b3']
for i, (a, b) in enumerate(zip(a_list, b_list)):
    print(i, a, b)
