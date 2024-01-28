# install python : https://www.python.org/downloads/
# install xampp : https://www.apachefriends.org/download.html
# open cmd :-> install -> pip install pymysql

import pymysql as mq

#	Server Name -> localhost
#	Username ->		root
#	Password ->		''

myobj = mq.connect(host="localhost",user="root",password="")

cursorobj=myobj.cursor()

try:
	db="create database school"
	cursorobj.execute(db)
	print("database created ")

except mq.Error as e:
	print(f"database error..{e}")

finally:
	myobj.close()

# Mysql Data type:
# INT 			(Len:11) number
# BIGINT		(len: 20) number->phone number


# VERCHAR		(len:0-255)		string
# TEXT 			(len:0-60000) 		string
# LONGTEXT				60000+---		string

# DATE 			YYYY-MM-DD
# DATETIME		YYYY-MM-DD HH:MM:SS
# TIMESTAME 	CurrentTime
# TINYINT 		(3)
# TIME 			HH:MM:SS
# YEAR 			YYYY->2022

