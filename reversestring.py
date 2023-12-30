a=input('enter a string:-')
i=0
out=''
while i<len(a):
   #     out=a[i]+out
         out=out+a[len(a)-i-1]
         i+=1
print(out)     