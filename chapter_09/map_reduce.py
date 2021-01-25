from functools import reduce


def f(x):
    return x ** 2


def g(x, y):
    return x ** 2 + y ** 2


def asterisk_test_1(a, *args):
    print(a, args)
    print(type(args))


def asterisk_test_2(a, **kargs):
    print(a, kargs)
    print(type(kargs))


print(f(4))
print((lambda x, y: x+y)(1, 10))  # lambda

ex = [1, 2, 3, 4, 5]
print(list(map(f, ex)))
print(list(map(g, ex, ex)))

print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))


def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))


print(factorial(5))  # 람다함수는 권장하지 않는다. 웬만하면 쓰지 않는것이 좋다.
asterisk_test_1(1, 2, 3, 4, 5)
asterisk_test_2(1, b=2, c=3, d=4)
