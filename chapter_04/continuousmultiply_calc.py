while 1:
    print("Enter number!")
    input_num=int(input())
    if input_num==0:
        break
    elif not(1<=input_num and 9>=input_num):
        print('Wrong num enter again')
        continue

    for i in range(1,10):
        print(input_num,'*', i,'=',input_num*i)
print('Exit')
