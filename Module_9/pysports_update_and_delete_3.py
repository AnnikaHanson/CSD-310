import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost",
database='pysports', 
user='root',
password='ntA6KNFQGBZeRv2rVT7K')

cursor = connection.cursor()

query = "DELETE FROM player WHERE first_name = 'Smeagol'"
cursor.execute(query)
connection.commit()
print(cursor.rowcount, "record(s) affected")

connection.close()

