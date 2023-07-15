import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost",
database='pysports', 
user='root',
password='ntA6KNFQGBZeRv2rVT7K')

cursor = connection.cursor()

sql = "INSERT INTO player (player_id, first_name, last_name, team_id) VALUES (%s, %s, %s, %s)"
val = ("021", "Smeagol", "Shire Folk", "2")

cursor.execute(sql, val)
connection.commit()

print(cursor.rowcount, "record(s) affected")

connection.close()
