
#	left join keyword returns all record from the left table(A), 
#	and the matched records from the right table (B)

import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="", database="school")
mycursor=mysql.cursor()

print("{:<15} {:<20} {:20}".format("State Id", "State Name", "Country name"))

try:
	sql="SELECT state.state_id,state.state_name,country.country_name from state left join country on state.country_id=country.country_id"
	mycursor.execute(sql)
	sdata=mycursor.fetchall()
	for s in sdata:
	
		print("{:<15} {:<20} {:<20}".format(s[0],s[1],s[2]))
except:
	print("error..")