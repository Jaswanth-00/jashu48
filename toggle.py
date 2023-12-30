a=input('enter a toggle')
i=0
out=''
while i<len(a):
    if a[i]=='1':
        out=out+'0'
    else:
        out=out+'1'
    i+=1
print(out)        
