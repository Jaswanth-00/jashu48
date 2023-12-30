                                 # global variables
#a=10
#b=20
#def sample(a):
#    global a,b # global keyword should be first in method area or function
#    b=90
#    print(a)#2
#    print(b)#3
#    print(a)#4
#print(a) #1
#sample()
#print(a)#5



                      # local variabels

a=10
def sample():
    b=20
    
    def inner():
        nonlocal b # the nonlocal keyword is used to modify the local variables inside the nested function
        c=30
        b=40
        print(b)#2
        print(c)#3
    print(b)#1
    inner()
    print(b)#4
sample()

