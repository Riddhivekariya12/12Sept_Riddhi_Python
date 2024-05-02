import pymysql  
 
try:
    dbcon=pymysql.connect(host="localhost",user='root',password=[],database=("tempdb.db"))

except:
    pymysql 


# create table

tbl_create="create table studinfo(id integer primary key autoincrement,name text,city text)"
try:
    dbcon.execute(tbl_create)
    print("Table created successfully!")
except Exception as e:
    print(e)

# Insert Records
insert_data="insert into studinfo(name,city)values('riddhi','rajkot'),('meet','baroda'),('niraju','morbi'),('dhanvi','surat'),('harsh','ahmedabad'),('pratik','rajkot')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)

