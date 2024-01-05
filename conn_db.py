#!/usr/bin/python

import os
import mysql.connector as myconn

db_user = os.environ.get("DB_USER")
db_passwd = os.environ.get("DB_PASSWD")
db_name = os.environ.get("DB_NAME")
db_server = os.environ.get("DB_SERVER")

show_table = "SHOW TABLES"

conn = myconn.connect(user=db_user,
                     password = db_passwd,
                     host = db_server,
                     database = db_name)

cursor = conn.cursor()

cursor.execute(show_table)

resultado = cursor.fetchall()

print(resultado)

for table in resultado:
    print(table)

cursor.close()

conn.close()
