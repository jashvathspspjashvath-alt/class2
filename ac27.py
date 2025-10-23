s=input('enter')
n=len(s)
res=''

for i in range(n-1,-1,-1):
    res+=s[i]
print(res)