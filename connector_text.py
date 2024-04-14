import mysql.connector


connection = mysql.connector.connect(
    user= 'root',
    database = 'sample',
    password = 'password'
)

cursor = connection.cursor()
testQuery = ("SELECT * FROM dnd")
cursor.execute(testQuery)


for row in cursor:
    print(row)


insertQuery = ("INSERT INTO smample.dnd (Game_id, sesstions, player_count, champaigns) VALUES (5, '6th', 6, 'slivins tain')")
cursor.execute(insertQuery)

cursor.execute(testQuery)


for row in cursor:
    print(row)

connection.commit()


cursor.close()
connection.close()