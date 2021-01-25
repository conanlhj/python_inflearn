sentence = 'I love you'
reverse_sentence = ''

for char in sentence:
    reverse_sentence = char + reverse_sentence
print (reverse_sentence,)

for char in sentence:
    reverse_sentence = reverse_sentence + char
print (reverse_sentence)
