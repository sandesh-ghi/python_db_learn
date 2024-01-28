import pymysql as mq
conn=mq.connect(host="localhost",user="root",password="", database="school")

mysqlc=conn.cursor()

# Table student (St_id,st_name,st_class,St_email)

try:
	tblcreate="create table student(id INT primary key auto_increment, name varchar(20), class varchar(10), email varchar(30))"

	mysqlc.execute(tblcreate)
	print("table create")
except mq.Error as e:
	print(f"table already exists.{e}")
finally:
	conn.close()

