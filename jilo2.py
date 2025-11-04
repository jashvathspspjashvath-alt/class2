a=int(input('enter a num:'))
num=1
print('\nfloyd triange')
for i in range(1,a+1):
    for j in range(1,i+1):
        print(num, end='')
        num +=1
    print()