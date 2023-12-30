
           # method:2=> by def inside the class

#class Employee:
#    company='tesla'
#    ceo    ='elon musk'
#    def insert_member(self,name,age,sal,eid):  
#        self.name=name
#        self.age=age
#        self.sal=sal
#        self.eid=eid

#jashu=Employee()
#mohan=Employee()
#raju=Employee()
#Employee.insert_member(jashu,'jashu',22,50000,111)
#Employee.insert_member(mohan,'reddy',30,40000,222)
#raju.insert_member('raju',40,45000,333)



                      #method:3=>init method
                  
class Employee:
    company='tesla'
    ceo    ='elon musk'
    def insert_member(self,name,age,sal,eid):  
        self.name=name
        self.age=age
        self.sal=sal
        self.eid=eid

jashu=Employee('jashu',22,50000,111)
















