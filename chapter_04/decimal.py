print("give me number")
decimal = int(input())
result = ''
while (decimal>0):
    remainder = decimal % 2
    print(remainder)
    decimal = decimal // 2
    result = str(remainder) + result
print(result)
