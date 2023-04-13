import mysql.connector


def crete_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='qwerty',
        database='aws_instances'
    )
