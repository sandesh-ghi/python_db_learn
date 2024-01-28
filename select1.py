import pymysql as mq

mysql=mq.connect(host="localhost",user="root",password="", database="school")

mycursor=mysql.cursor()


# mycursor.execute("SELECT * FROM student")
# print("{:<15} {:<20} {:<20} {:10}".format("ID", "Name", "Class", "Email")) 		# 
print("{:<15} {:<20}".format("ID", "Name"))


try:
	# sql="Select * from student"			# show all data 
	sql="Select id,name from student"		# show id and name
	mycursor.execute(sql)
	# sdata=mycursor.fetchall()
	sdata=mycursor.fetchone()		# show one row data
	print("{:<15} {:<20}".format(sdata[0],sdata[1])) 		
	

	
	# for s in sdata:
	 	# print("{:<15} {:<20} {:<20} {:10}".format(s[0],s[1],s[2],s[3]))
	 	# print("{:<15} {:<20}".format(s[0],s[1]))

except mq.Error as e:
	print(f"error..{e}")

finally:
	mysql.close()
