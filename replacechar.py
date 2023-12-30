string=input('enter a string:-')
i=0
out=''
while i<len(string):
    if not( 'A'<=string[i] <= 'Z' or 'a'<= string[i]<='z' or'0'<=string[i]<='9'):
        out=out+'_'
    else:
        out=out+string[i]  
    i+=1     
print(out)        