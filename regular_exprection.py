

import re
# a='The date is 04/01/2024'
# data=re.findall('\d',a)
# print(data)


# a='The 4 date 9 is 04/01/2024'
# data=re.findall('\d{2}',a)                       # can't check a single digitnumbers in it
# print(data)                                      #o/p:    ['04', '01', '20', '24'] 



# a='The 4 date 9 is 04/01/2024'
# data=re.findall('[24680]',a)                    # to get even number   ['4', '0', '4', '0', '2', '0', '2', '4']        
# print(data)


# a='The 4 date 9 is 04/01/2024'
# data=re.findall('\d[24680]',a)                    #-\d[24680] -to get the double no.s          
# print(data)                                       #o/p:['04', '20', '24']


# a='123 67 The 4 date 9 is 04/01/2024'
# data=re.findall('\d+',a)                    # o/p:['4', '9', '04', '01', '2024']  
# print(data)

#write the pattern to extract pan card no.

# a='ABCDE1234HJRTH789TOMSTfghjjj8FGHJJ3448Y'         #  ['ABCDE1234H', 'FGHJJ3448Y']
# data=re.findall('[A-Z]{5}\d{4}[A-Z]',a)                      
# print(data)

# a='Ap41AB9999'
# data=re.findall('Ap[0-4]\dAB\d{4}',a)                        #  ['Ap01AB9999']             
# print(data)

# a='+91-9845012390'
# data=re.findall('[+]\d{2}[-]\d{10}',a)                                     
# print(data)

a='abc123@gmail.com'
data=re.findall('[a-z]+[a-z0-9]*@gmail.com',a)                                     
print(data)

a='ABCDEFGIJKABC'
data=re.findall('[A-G][]',a)                                     
print(data)




















































































