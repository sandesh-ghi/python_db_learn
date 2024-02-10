	# Inner Join select all rows from both particiapting tables as long ad there is a math between the columns
import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="", database="school")
mycursor=mysql.cursor()

print("{:<15} {:<20} {:20}".format("State Id", "State Name", "Country name"))

try:
	sql="SELECT state.state_id,state.state_name,country.country_name FROM state INNER JOIN country on state.country_id=country.country_id"
	mycursor.execute(sql)
	sdata=mycursor.fetchall()
	for s in sdata:
	
		print("{:<15} {:<20} {:<20}".format(s[0],s[1],s[2]))
except:
	print("error..")