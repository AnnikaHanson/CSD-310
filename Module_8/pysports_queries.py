import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost",
database='pysports', 
user='root',
password='ntA6KNFQGBZeRv2rVT7K')
    
if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)


    ##Query##
    #SELECT team_id, team_name, mascot FROM team;

    ##cursor##
    #cursor = db.cursor()
    #cursor.execute("SELECT team_id, team_name, mascot FROM team”)

