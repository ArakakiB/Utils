
from mysql.connector import (connection)
db_connection = connection.MySQLConnection(host='127.0.0.1', user='root', password='1590', database='comandos_sql')
db_connection.close()