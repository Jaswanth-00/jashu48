a=input('enter a string')
i=0
out=''
while i<len(a):
    if '0'<=a[i]<='9':
        out=out+a[i]
    i+=1
print(out)        