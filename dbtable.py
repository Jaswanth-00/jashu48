import pymysql
con=pymysql.connect(user='root',password='raju@903091',port=3306,database='pymysql')
cursor=con.cursor()
def create_table():
    try:
        query='''
        create table customer(
        id int primary key,
        name varchar(100),
        mobile bigint,
        balance bigint
        );
        '''
        cursor.execute(query)
    except pymysql.err.OperationalError as e:
        print(f'{e}')

def insert_record():
    query='insert into customer(id,name,mobile,balance) values(1,"reddy",9076590310,50000)'
    cursor.execute(query)
    con.commit()
#insert_record()
def get_record():
    query='select*from customer'# to call the insert_record function
    cursor.execute(query)
    records=cursor.fetchall()
    print(records)
    
def insert_dynamic(cid,name,mobile,balance):
    record=(cid,name,mobile,balance)
    query="insert into customer(id,name,mobile,balance) values(%s,%s,%s,%s)"
    cursor.execute(query,record)
    con.commit()                               #o/p: insert_dynamic(valuse----------)
                                               # get_record() -is used to get inserted recordes
def drop_record(cid):
    query='delete from customer where id={cid}'
    cursor.execute(query)
    con.commit()
    print('records removed')                     # to drop thr record
















































































