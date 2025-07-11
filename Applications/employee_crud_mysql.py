import pymysql
import sys

def connect_db():
    connection = None
    try:
        connection = pymysql.connect(
            host ="localhost",
            user = "root",
            password = "Akshat@2809",
            database = "db1",
            port = 3306,
            charset ="utf8"
        )
        print('Database connected successfully!')
    except pymysql.Error as e:
        print(f"Connection to database failed: {e}")
        return None
    return connection

def disconnect_db(connection):
    if connection:
        try:
            connection.close()
            print('DB disconnected')
        except pymysql.Error as e:
            print(f'DB disconnection failed: {e}')
    else:
        print('No active database connection to disconnect.')

def create_db(connection):
    query = 'CREATE DATABASE IF NOT EXISTS db1'
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print('Database created (or already exists).')
    except pymysql.Error as e:
        print(f'Database creation failed: {e}')
    finally:
        if cursor:
            cursor.close()

def create_table(connection):
    query = '''
    CREATE TABLE IF NOT EXISTS employee (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        designation VARCHAR(30),
        phone_number BIGINT UNIQUE,
        salary FLOAT,
        commission FLOAT DEFAULT 0,
        years_of_experience TINYINT,
        technology VARCHAR(30) NOT NULL
    )
    '''
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print('Table "employee" created (or already exists).')
    except pymysql.Error as e:
        print(f'Table creation failed: {e}')
    finally:
        if cursor:
            cursor.close()

def read_all_employees(connection):
    query = 'SELECT * FROM employee'
    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        if not rows:
            print('No employees found in the table.')
        else:
            print('--- All Employees ---')
            for row in rows:
                print(row)
            print('All rows retrieved successfully.')
    except pymysql.Error as e:
        print(f'Rows retrieval failed: {e}')
    finally:
        if cursor:
            cursor.close()

if __name__ == "__main__":
    main_connection = None
    try:
        main_connection = connect_db()

        if main_connection:
            create_db(main_connection)
            create_table(main_connection)
            read_all_employees(main_connection)
        else:
            print("Cannot proceed with database operations due to connection failure.")

    except Exception as e:
        print(f"An unexpected error occurred in the main process: {e}")
    finally:
        disconnect_db(main_connection)