def asterisk_test(a,b,*args):
    return args

def asterisk_test_2(*args):
    x,y,z=args
    return x,y,z

def kwargs_test_1(**kwargs):
    print(kwargs)
    print(kwargs["first"])

def kwargs_test_2(**kwargs):
    print(kwargs)
    print("First value is {first}".format(**kwargs))
    print("Second value is {second}".format(**kwargs))
    print("Third value is {third}".format(**kwargs))

def kwargs_test_3(one, two, *args, **kwargs):
    print(kwargs)
    print(args)
    print(one+two+sum(args))


# print(asterisk_test(1,2,3,4,5))
# print(asterisk_test_2(1,2,3))

kwargs_test_3(3,4,5,6,7,8,9,10,second=3, first=4, third=5)
