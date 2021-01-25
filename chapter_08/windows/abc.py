a = '..-  --. --.'.split(' ')
result = ''
for i in a:
    if i == '':
        result += ' '
    else:
        result += i
print(result)
