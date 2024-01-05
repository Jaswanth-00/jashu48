import csv
# with open('mca.csv','w',newline='') as csvfile:
#     data=csv.writer(csvfile)
#     data.writerow(['id','name','mobile','email'])                    .To write the file
#     data1=[[1,'venu',345678,'vanu@gmail.com'],
#            [2,'abhi',3453456678,'vanu@gmail.com']
#     ]
#     data.writerow(data1)


# with open('mca.csv','r') as csvfile:
#     data=csv.reader(csvfile)
#     for i in data:                           .To read the file
#         print(i)



# with open('mca1.csv','w',newline='')as csvfile:
#     fieldnames=['id','name','mobile','email']
#     data=csv.DictWriter(csvfile,fieldnames)
#     data.writeheader()
#     rows=[{'id':1,'name':'jashu','mobile':987654321,'email':'jashu@gmail.com'},
#          {'id':2,'name':'reddy','mobile':987659876,'email':'reddy@gmail.com'}
#     ]
#     data.writerows(rows)



with open('mca1.csv','r') as csvfile:
    data=csv.DictReader(csvfile)
    for row in data:
        print(row['name'])



