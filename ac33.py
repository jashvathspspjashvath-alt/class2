start=int(input('enter a str num:'))
end=int(input('enter the ending num:'))
print(start,end)
for num in range(start,end +1):
 if num >1:
  for i in range(2,int(num**0.5)+1):
   if num %i==0:
    break
else:
   print(num)