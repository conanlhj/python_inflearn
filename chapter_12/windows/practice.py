f = open('1984.txt', "r", encoding="utf8")
contents = f.read()
f.close()
for char in '''-,.?!''""():;—‘’''':
    contents = contents.replace(char, '')
print(contents)

f = open('werwer.txt', "w", encoding="utf8")
f.write(contents)
f.close()
