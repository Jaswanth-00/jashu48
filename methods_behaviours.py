#class cube:
#    def __init__(self,side):
#        self=side=side
#    def volume(self):
#        return self.side**3
#    def surface(self):
#        return 6*self.side**2




class sbi:
    brand='palamaner'
    ifse='sbi00222'
    manager='reddy'
    loc='chittoor'
    def __init__(self,name,mob,acc,pan,bal):
        self.name=name
        self.mobile=mob
        self.acc0unt=acc        
        self.pann=pan
        self.ball=bal

    def credit(self,amt):
        self.balance+=amt
        
    def debit(self,amt):
        self.balance-=amt

    def update_mob(self,mob):
        self.mobile=mob

    @classmethod
    def change_mgr(cls,new):   # class method
        cls.manager=new
    @staticmethod
    def add(a,b):      #static method
        return a+b

sreddy=sbi('SR reddy',9099346970,98345671235,'SRMR0000m',12345678)
raju=sbi('RR raju',90993469345,983453331235,'RRR0000r',34567890)








