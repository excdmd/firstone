import pymysql
import time
tt=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
db=pymysql.connect(host='localhost',user='root',password='root',port=3306,db='test_db')

print(db.get_server_info(),db.get_host_info())

#1、创建游标
cur=db.cursor()

myage =55
db.begin()
#sql="INSERT INTO student(NAME,score,tim) VALUES ('%s',%d,'%s')"
#sql="insert into people (id,name,age,sex,salary,address) values (6,'ken',36,'男',666000,'香港')"
sql="update people set age="+ str(myage) +",sex='男',salary='10',address='西安' where id='6';"

data=('HW',90,tt)
try:
  cur.execute(sql)
except Exception as e:
  print(e)
  db.rollback()
else:
  db.commit()
finally:
  cur.close()
  db.close()
