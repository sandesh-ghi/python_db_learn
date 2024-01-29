import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="", database="school")
mycursor=mysql.cursor()

# mycursor.execute("SELECT * FROM student")
print("{:<15} {:<20} {:<20} {:10}".format("ID", "Name", "Class", "Email")) 		# 

try:
	name=input("Enter the student Name: ")
	class_name=input("Enter the class name: ")

	#-> like : use search only letter 

	# sql="SELECT * FROM student WHERE name='"+name+"'"	
	# sql="SELECT * FROM student WHERE name like'%"+name+"%' and class='"+ class_name+"' "				
	sql="SELECT * FROM student WHERE name like'%"+name+"%' or class='"+ class_name+"' "		# when enter two data but match only one display result in OR condition		

	mycursor.execute(sql)
	sdata=mycursor.fetchall()
			
	for s in sdata:
	 	 print("{:<15} {:<20} {:<20} {:10}".format(s[0],s[1],s[2],s[3]))
	 
except mq.Error as e:
	print(f"error..{e}")

finally:
	mysql.close()
