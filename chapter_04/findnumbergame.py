import random
guess_number = random.randint(1, 100)
print(guess_number)
# print('guess number!')
user_input = int(input())
while (user_input != guess_number):
    if user_input > guess_number:
        print('down')
    else:
        print('up')
    user_input = int(input())
print('wow!')
