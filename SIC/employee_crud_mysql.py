import pymysql

def connect_db():
    connection = None
    try:
        pymysql.Connect(host ="localhost", user = "root", password = "Akshat@2809", database = "db1", port = 3306, charset ="utf8")
        print('Database connnected')
    except:
        print("Connnection to database failed")
        raise
    return connection

connection = connect_db()