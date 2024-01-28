import pymysql as mq

mysql=mq.connect(host="localhost",user="root",password="",database="school")

cursorobj=mysql.cursor()

id=input("enter stdent id: ")
sql="DELETE FROM student WHERE id=%s"


try:
	cursorobj.execute(sql,id)
	mysql.commit()
	print ("Student Deleted.")

except: 
	print("Error..")
	 