#var_name=[ i for i in range(1,10)]
#print(var_name)

#a=[i*i for i in range(1,10)]
#print(a)


#from math import factorial
#a=[factorial(i) for i in range(1,7)]
#print(a)

#a=["abcd",{1:2},[4,5,6],{4,7},(9,8,7)]
#a=[len(i) for i in a]
#print(a)

#a=[i**3 for i in range(1,25) if i%3==0]
#print(a)

#b=([1,2,4,6],(1,2),{4,6,7},{2:1,4:2,1:3},'efgh')
#b=[len(i)  for i in b]
#print(b)

#a=[i for i in range(1,100) if i%3==0  if i%2==0 if i%5==0]
#print(a)

#a=[i**2 if i%2==0 else i**3 for i in range(1,20)]
#print(a)

         # wap to store multiple of 2,3,4 in a nested list collection:-
# minimum one loop one condition
#b=[[i*j for j in range(1,11)] for i in [2,3,4]]
#print(b)

#a={ i:i*2 for i in range(1,5)}
#print(a)

#a='xyz'
#b='123'
#x={i:j for i,j in zip(a,b) }
#print(x)

a='ABCDEF'
#x={j:i for i,j in enumerate(a) if i%2==0 } 
         # OR
x={a[i]:i for i in range(len(a)) if i%2==0}
print(x)





