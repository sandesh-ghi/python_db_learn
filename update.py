import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="school")
cursorobj=mysql.cursor()
name=input("Enter name: ")
class_name=input("Enter class: ")
email=input("enter email: ")
st_id=input("Enter student id: ")

sql="UPDATE student SET name=%s, class=%s, email=%s where id=%s"
data=(name, class_name, email, st_id)

try:
	cursorobj.execute(sql,data)
	mysql.commit()
	print("data updated")
except:
	print("error.. ")


