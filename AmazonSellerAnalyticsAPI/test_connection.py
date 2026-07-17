from database import Database

db = Database()

connection = db.connect()

if connection:
    print("Database Connection Successful")
else:
    print("Database Connection Failed")