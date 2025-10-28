num= int(input('enter a number:'))
order = len(str(num))
summ = 0
temp = num
while temp >0:
    digit = temp % 10
    summ += digit ** order
    temp //= 10
if num == summ:
    print(num,' an armstrong number')
else:
    print(num, 'is not armstrong number')