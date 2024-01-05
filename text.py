import re
# with open(r"N:\jashu48\text.txt",'r') as file:
#     data=file.read()
#     out=re.findall('[Aa][a-z]*',data)
#     print(out)#print(len(out))


# with open(r"N:\jashu48\text.txt",'r') as file:
#     data=file.read()
#     data1=re.split(' ',data)
#     count=0
#     words=[]
#     for i in data1:
#         out=re.match('^a',i)
#         if out:
#             words+=[i]
#             count+=1
#     print(count)
#     print(words)

with open(r"N:\jashu48\text.txt",'r') as file:
    data=file.read()
    data1=re.sub('a','@',data)
    file.write(data1)













































































