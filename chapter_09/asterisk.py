def asterisk_test_1(a, *args):
    print(a, args)
    print(type(args))


def asterisk_test_2(a, args):
    print(a, *args)
    print(type(args))


def asterisk_test_4(a, args):
    print(a, *args)
    print(type(args))


def asterisk_test_3(a, b, c, d):
    print(a, b, c, d)


asterisk_test_1(1, *(2, 3, 4, 5, 6))
asterisk_test_2(1, (2, 3, 4, 5, 6))

a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c)

data = ([1, 2], [3, 4], [5, 6])
print(data)
print(*data)

quote = 'Hello World!'
print(quote)
print(*quote[2])

for data in zip(*([1, 2], [3, 4], [5, 6])):
    print(data)

data = {'b': 1, 'c': 2, 'd': 3}
asterisk_test_3(10, **data)
