import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'vuk@2004'

	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE hotel_data")

print("All Done!")