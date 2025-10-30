num = int(input('ent a num'))
num=str(num)
length= len(num)
if length % 2==0:
    mid1 = int(num[length // 2-1])
    mid2= int(num[length // 2])
    product = mid1 * mid2
    print({mid1},{mid2})
else:
    mid =int(num[length // 2])
    product = print({mid})
print(product)
