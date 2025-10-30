word = input('enter a words:')
a=0
char = word[a]
count = 0
b = 0
while b< len(word):
    if word[b] == char:
        count+= 1
    b += 1
    if word.index(char) == a:
        print({char},{count})

    a += 21