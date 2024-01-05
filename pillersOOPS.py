                                             #1> Inheritance



               # i.single level inheritance


#class base:
#    a=10
#    b=20
#    def __init__(self,c):
#        self.c=c

#class derived(base):

#    def __init__(self,c,d,e):
#       # super().__init__(c)       # calling from  parent constructor to child constructor
#              # or
#        base. __init__(self,c)
        
#        self.d=d
#        self.e=e
#obj=derived(6,55,90)



             # ii.Multi level inheritance



#class Gparent:
#   a=10
#   b=20
#   def __init__(self,c):
#       self.c=c
#
#class parent(Gparent):
#
#   def __init__(self,c,d,e):
#       
#       super(). __init__(c)
#       
#       self.d=d
#       self.e=e
#
#class child(parent):
#
#   def __init__(self,c,d,e,f,g):
#       
#       super().__init__(c,d,e)
#
#       self.f=f
#       self.g=g
#obj=child(6,55,90,91,92)



                                 # iii.hierarchial inheritance



#class college:
#   name='mother theresa'
#   def __init__(self,degree,pg):
#       
#       self.degree=degree
#       self.pg=pg
#
#class cources(college):
#   def __init__(self,degree,pg,bsc,bcom,mca,mba):
#       super().__init__(degree,pg)
#
#       self.bsc=bsc
#       self.bcom=bcom
#       self.mca=mca
#       self.mba=mba
#0bj=cources(23000,30000,40000,50000,35000,450000)



                                  #iv.multiple inheritance

#class add:
#   @staticmethod
#   def add(a,b) :
#       return a+b
#class sub:
#   @staticmethod
#   def sub(a,b) :
#       
#       return a-b
#   
#class cal(add,sub):
#   pass
#obj=cal(add,sub)
#obj.add(2,3)
#obj.sub(5,2)
    

                           # v.hibrid inheritance


#class add3:
#  @staticmethod
#  def add(a,b,c) :
#      return a+b+c
#class add2:
#  @staticmethod
#  def add(a,b) :
#      return a+b
#class add(add2,add3):
#   pass
#cclass sub2:
#  @staticmethod
#  def sub(a,b) :
#      
#      return a-b
#  
#class cal(add,sub2):
#  pass
#obj=cal()
#obj.add(2,3)
#obj.sub(5,2)


                                            #2> POLYMORPHISM

#class model:
#   @staticmethod
#   def add(a,b):
#       return a+b
#   @staticmethod
#   def add(a,b,c):
#       return a+b+c
#obj=model()
#obj.add(1,2,3)


from abc import ABC,abstractmethod
class car(ABC):
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
        self.speed=0
    @abstractmethod
    def stop():
        pass
    @abstractmethod
    def speed_up():
        pass
    @abstractmethod
    def speed_down():
        pass
class bmw(car):
    def speed_up(self):
        self.speed+=5
    def speed_down(self):
        self.speed-=5
    def stop(self):
        self.speed=0
class tata(car):
    def speed_up(self):
        self.speed+=2
    def speed_down(self):
        self.speed-=2
    def stop(self):
        self.speed=0
bmw1=bmw('x7','black',5000000)
nexon=tata('nexon ev','white',10000)
    


