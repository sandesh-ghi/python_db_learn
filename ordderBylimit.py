import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="school")
mycursor=mysql.cursor()

print("{:<15} {:<20}".format("ID", "Name"))

try: 
	# sql="SELECT * FROM student "
	# ASC , DESC
	# limit

	sql="SELECT * FROM student order by name DESC "	
	
	# sql="SELECT * FROM student order by id DESC  limit 0,2"					

	mycursor.execute(sql)
	sdata=mycursor.fetchall()

	for s in sdata:
		print("{:<15} {:<20}".format(s[0],s[1]))

except mq.Error as e:
	print(f"Error.. {e}")

finally:
	mysql.close()
