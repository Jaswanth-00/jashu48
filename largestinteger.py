a=[1,5,8,35,67,89,99]
out=a[0]
out2=a[0]
for var in a:
    if out<var:
        out=var
for var in a:
    if out2<var and var!=out:
        out2=var
print(out,out2)
#second method
#a=[1,5,8,35,67,89,99]
#out=a[0]
#out2=a[0]
#for i in a:
# if out<i
#out2=out
#out=i
#elif out2>i:
 #   out2=if
#print(out,out2)
