                                    # arguments


       #=> add minimum 2 no. and maximum 5 no. using functions

#def add(a,b,c=0,d=0,e=0):
#    return a+b+c+d+e
#out=add(1,2,3,4,5)
#print(out)

     #=> example:1
#def add(a,b,c=0):
#    print('a:-',a)
#    print('b:-',b)
#    print('c:-',c)
 #   return a+b+c
#out=add(a=3,c=5,b=7)
#print(out)


 #=> out=add(3,a=4,c=5) we get type error 
#=> out=add(a=4,b=7,6) we get syntex error 
#=> out=add(3,9,7,c=9) we get type error 


                            # packing
    # arguments
    
   #=> example:1
 
#def add(*args):
#    out=0
#    for i in args:
#        out+=i
#    return out
#res=add(3,9,3,667,5,99,65)
#print(res)


     #=> example:2

# def add(*args):
#   print(args)
#add()
# output=()


                           # keyword arguments
      #=> example:1

#def add(*args,**kwargs):
#    print(args)
#    print(kwargs)
#add(a=10)

     #=> example:2

#def add (*args,**kwargs):  #=> def add(**kwargs,*args)  we get syntax error
#    print(args)
#    print(kwargs)
#add(3,5,a=10,b=49)

       #=>example:3

#def add (a,*args,**kwargs):
#    print(args)
#    print(kwargs)
#add(3,5,b=49)

       #=> example:4

#def add (a,*args,**kwargs):
#    print(a,args)
#    print(kwargs)
#add(3)

       #=> example:5

#def add (b=0,*args,**kwargs):
#    print(b,args)
#    print(kwargs)
#add(3,5)



                                   # unpacking

   #=> example:1

#def add(a,b,c):
#    print(a)
#    print(b)                      # o/p: 3  4  9
#    print(c)
#add(*[3,5,9])   # we are unpacking 


      #=> example:2

#def add(a,b,c,d):
#    print(a)
#    print(b)                      # o/p: type erroe
#    print(c)
#add(*[3,5,9])


       #=>  example:3


#def add(a,b):
 #   print(a)
 #   print(b)                      # o/p: type error
#    print(c)
#add(*[3,5,9])

       #=> example:4

#def add(a,b,c):
#    print(a)
#    print(b)                             # o/p: a   b    c
#    print(c)
#add(*{'b':34,'c':45,'a':33})

         #=> example:5

#def add(a,b,c):
#    print(a)
#    print(b)                             # o/p: 33   34   45
#    print(c)
#add(**{'b':34,'c':45,'a':33})            # in dictionary only we get **

     #=> example:6

#def add(a,b,d):
#    print(a)
#    print(b)                             # o/p: type error
 #   print(d)
#add(**{'b':34,'c':45,'a':33})



                          #  recursion

     #=> example:7

def sum(a,b):
    if a==b:
        return a
    return a+sum(a+1,b)
out=sum(1,5)
print(out)                           # o/p: 55
    

