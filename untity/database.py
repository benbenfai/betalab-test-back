import mysql.connector

authdb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="",
  database="database"
)
