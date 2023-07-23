import mysql.connector

def connectdb():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='ltms'
    )
    return connection

def isconnected():
    return connectdb().is_connected()
    
