import mysql.connector
conn=mysql.connector.connect(user='root', password='Nopassword01', host='52.165.29.136', database='autohome')
cursor=conn.cursor()
query=("SELECT * from switch")
cursor.execute(query)
result=cursor.fetchone()
print result
print result[1]
print result[2]
print result[3]
print result[4]
print result[5]
conn.close()
