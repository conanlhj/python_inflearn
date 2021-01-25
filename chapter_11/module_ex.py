import fah_converter as fconv
# from fah_converter import convert_c_to_f  <- 모듈에서 특정 함수 또는 클래스만
# from fah_converter import *  <- 모듈에서 모든 함수 또는 클래스 호출

print('Enter a celsius value: ')
celsius = float(input())
fahrenheit = fconv.convert_c_to_f(celsius)
print("That's", fahrenheit, " degrees Fahrenheit")
print(fconv.A)
