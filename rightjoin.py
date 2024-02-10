#	This means that a right join returns all the values from the right table, plus matched values from the left table.

import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="", database="school")
mycursor=mysql.cursor()

print("{:<15} {:<20} {:20} {:<20} {:20}".format("User Id", "User Name", "User Address", "Order Id","order Amount"))

try:
	sql="SELECT users.user_id,users.user_name,users.user_address, orders.order_id,orders.order_amount from users right join orders on users.user_id=orders.user_id" 
	mycursor.execute(sql)
	sdata=mycursor.fetchall()
	for s in sdata:
	
		print("{:<15} {:<20} {:<20} {:<20} {:<20}".format(s[0],s[1],s[2],s[3],s[4]))
except:
	print("error..")