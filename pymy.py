  # to create database

import pymysql
conn=pymysql.connect(user='root',password='raju@903091',port=3306)
cursor=conn.cursor()
query='create database pymysql'
cursor.execute(query)



