import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost",
database='pysports', 
user='root',
password='ntA6KNFQGBZeRv2rVT7K')

cursor = connection.cursor()

query="SELECT player.player_id, player.first_name, player.last_name, team.team_name FROM player LEFT OUTER JOIN team ON player.team_id=team.team_id"

cursor.execute(query)
rows=cursor.fetchall()

for x in rows:
    print(x)

connection.close()

