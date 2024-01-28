import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="", database="school")

mycursor=mysql.cursor()


try:
	# id, name, class, email
	ins="INSERT INTO student(name,class,email) values(%s,%s,%s)"
	# t=("ram",'12th','ram@gmail.com') 					-> single row insert data in tuple
	t=[("shyam",'10th','shyam@gmail.com'),("hari",'11th','hari@gmail.com')] # ->  multi row data insert in list 
	mycursor.executemany(ins,t)													#-> to change execute-> executemany in multi row data insert
	mysql.commit();
	print("Insert data")

except:
	print("Error..")


