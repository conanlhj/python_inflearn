for i in range(10):
    try:
        print(i, 10//i)
    except ZeroDivisionError:
        print('Not divided by 0')
    finally:
        print(i+1, '번 루프 끝')
