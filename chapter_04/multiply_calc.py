print('구구단 몇단을 계산할까요?')
input_num = int(input())
print('구구단 {}단을 계산합니다.'.format(input_num))
for i in range(1,10):
    print(input_num,'*',i,'=',input_num*i)
