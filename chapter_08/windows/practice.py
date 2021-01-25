temp = list('This is Gachon!!')
remove_mark = list('.,?!')
for i in remove_mark:
    while i in temp:
        temp.remove(i)
result = ''.join(temp)
result = result.strip()
result = result.upper()
print(result)
print(list(result))
