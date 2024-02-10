
#	Equi join returns the matching column values of the associated tables. it uses a comparison operator in where clause to refer equality.
import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="", database="school")
mycursor=mysql.cursor()

print("{:<15} {:<20} {:20}".format("State Id", "State Name", "Country Name"))

try:
	sql="SELECT state.state_id,state.state_name,country.country_name from state,country where state.country_id=country.country_id"
	mycursor.execute(sql)
	sdata=mycursor.fetchall()
	for s in sdata:
	
		print("{:<15} {:<20} {:<20}".format(s[0],s[1],s[2]))
except:
	print("error..") 