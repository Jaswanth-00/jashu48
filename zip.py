                    # zip()
                           # by the help of zip() we can take more than one collections
#a='xyz'
#b='abc'
#out=""
#for i in range(len(a)):
#    out+=a[i]+b[i]
#print(out)


#a='xyz'                 # when a='xyz' and b='abcd'=>it performs minimum no.of iterations
#b='abc'
#out=''
#for i in zip(a,b):
#    print(i)
#print(out)

#a=[1,2,3]
#b=[4,5,6]
#c=[7,8,9]                           # o/p:[1, 4, 7, 2, 5, 8, 3, 6, 9]
#out=[]
#for i,j,k in zip(a,b,c):
#    out+=[i]+[j]+[k]
#print(out)

#a='ABC'
#b='456'
#out={}                      # o/p:{'A': '4', 'B': '5', 'C': '6'}
#for i,j in zip(a,b):
#    out[i]=j
#print(out)

         # enumerate

#a='abcd'
#out=''
#for i,j in enumerate(a):               #o/p:a0b1c2d3
#    out+=j+str(i)
#print(out)


# note:
#a=min(1,2,3,4)
#print(a)

#a=max(1,2,3)
#print(a)  

# note:
#a=reversed([1,2,3])  o/p:[3, 2, 1]
#print(list(a))


#a=sorted([2,4,1,7,5,6,3])
#print(a)         o/p:[1, 2, 3, 4, 5, 6, 7]


#a=reversed(sorted([1,2,5,8,3,6,]))
#print(list(a))

    # OR

#a=sorted([2,5,7,9,4,3,1],reverse=True)
#print(a)

from functools import reduce
a=[1,2,3]
def add(a,b):
    return a+b
out=reduce(add,a)
print(out)



















