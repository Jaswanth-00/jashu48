def sum_int(a):
    out=0
    for i in a:
        if type(i)==int:
            out+=i
    print(out)
sum_int([1,2,'a','s',3,5])
sum_int([5,'y',9])