import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    port=3306, 
    passwd='passwd123', 
    user='root'
    
    )

#prepare a cursor objec

cursorObject = dataBase.cursor()

#create database
cursorObject.execute("CREATE DATABASE discor")

print("database created")

