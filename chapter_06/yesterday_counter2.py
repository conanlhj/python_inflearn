f = open("yesterday.txt", 'r')
yesterday_lyric = ""
while 1:
    line = f.readline()
    if not line:
        break
    yesterday_lyric = yesterday_lyric + line.strip() + "/n"
f.close()

n_of_yesterday1 = yesterday_lyric.count("Yesterday")
n_of_yesterday2 = yesterday_lyric.count("yesterday")
print("Number of a Word 'Yesterday' :", n_of_yesterday1)
print("Number of a Word 'yesterday' :", n_of_yesterday2)
