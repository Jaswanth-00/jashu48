            # functions to count chrt in a string
chr='a'
a='abc234aa@34aa'
def strchr(a,chr):
    count=0
    for i in a:
        if i==chr:
            count+=1
    return(count) 
c=strchr(a,chr)
print(c)
