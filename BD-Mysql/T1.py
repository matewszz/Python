import mysql.connector

banco = mysql.connector.connect(
    host="localhost", user="root", passwd=""

)

print(banco)