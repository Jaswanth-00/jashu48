a=[1,9,11,23,65,75,84,90]
if len(a)%2==0:
    out=0
    for i in a:
        out+=i
else:
    out=1
    for i in a:
        out*=i
print(out)