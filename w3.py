def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b !=0:
        return a/b
    else:
        return'cannot divide by zero'

print('sel opr')
print('1add')
print('2sub')
print('3multi')
print('4divi')

choice = input('enter choice(1/2/3/4):')

num1=float(input('enter a num:'))
num2=float(input('ent sec number:'))

if choice =='1':
    print('result',add(num1,num2))
elif choice =='2':
    print('result',subtract(num1,num2))
elif choice =='3':
    print('result',multiply(num1,num2))
elif choice =='4':
    print('result',divide(num1,num2))
else:
    print('invalid chop')
   