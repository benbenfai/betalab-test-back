from database import authdb


cursor = authdb.cursor()
  
query1 = "select * from user;"
  
cursor.execute(query1)
  
table = cursor.fetchall()

for attr in table:
    print(attr)
  
cursor.close()
  
authdb.close()