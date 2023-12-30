                                  # GENERATORS
      #example:1


#def sqr_no (a,b):
 #   for i in range(a,b+1):
 #       yield i*2
 #       yield i**2
#out=sqr_no(5,15)
#print(list(out))

              # example:2


#b='asdfgertyuioAFGHJEVBNIBNOBU'
#def vowel_indx(b):
 #   for i in range(0,len(b)):
#        if b[i] in 'AEIOUaeiou':
#            yield b[i]
#            yield i
#d=vowel_indx(b)
#print(list(d))

               # example:3

#a=[1,[4,5,6],{7,8},'efg',{'a':1},9.5,12]

#def num(a):
 #   for i in a:
 #       if type(i) in [str,list,tuple,set,dict]:
 #           yield len(i)
 #       else:
 #           yield i
#c=num(a)
#print(list(c))

                # example:4

#a=[(1,2),[4,5,3],(11,12,13),[9,8,7,6],]
#def middle(a):
#      for i in a:
#            if len(i)%2==0:
#                  yield (i[0]+i[-1])/2
#            else:
#                  yield i[len(i)//2]
#out=middle(a)
#print(list(out))

                                  # FILTERS                
  # examlpe:5
#def fname(a):
#      if a%2==0:
#            return True
#      else:
#            return False
#out=filter(fname,[2,3,4,6,89,56,])
#print(list(out))
                               # OR
#print(list(filter(lambda a:a%2==0,[2,3,4,6,89,56,])))

              #  filtre numbers which are multiple by 5 and  3 in given collection
#def mul(a):
#      if a%3==0 and a%5==0:
#            return True
#      else:
#            return False
#out=filter(mul,range(1,200))                 o/p :[15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195]
#print(list(out))

                    #  OR

#print(list(filter(lambda x:x%5==0 and x%3==0,range(1,200))))


           # print only upper characters
#def upper(a):
#    if 'A'<=a<='Z':
#        return True
#    else:
#        return False
#out=filter(upper,'aBc@15J67GH')
#print(list(out))
                       #  OR

#print(list(filter(lambda a: 'A'<=a<='Z','aASD234DFGH')))



                          #=>       MAP       



#print(list(map(lambda a:2*a,[1,2,3,4])))
  # OR
#def double(a):
#    if a%3==0:
#      return 3**a
#    else:
#      if a%2==0:
#            return 2*a
#c=map(double,[2,3,4,6,8])
#print(list(c))


#def num(a):
#      if type(a) in [str,list,tuple,set,dict]:
#            return len(a)
#      else:
#            return a
#c=map(num,[1,(4,5),[7,9],{1:2}])
#print(list(c))

                              
                           
         # print odd numbers and find square of each number in given range(1,100)

#def odd(a):
#    if a%2!=0:
#        return True
#    else:
#        return False
#def square(b):
#    return b**2
#c=map(square,filter(odd,range(1,100)))
#print(list(c))






