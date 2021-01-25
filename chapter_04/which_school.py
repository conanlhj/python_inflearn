print("당신이 태어난 년도를 입력하세요")
year_born=int(input())
age=2020-year_born+1
print('your age is :',age)
if (age<26) and (age>=20):
    print('college')
elif (age<20) and (age>=17):
    print('high')
elif (age<17) and (age>=14):
    print('middle')
elif (age<14) and (age>=8):
    print('elementary')
else:
    print('not school')
