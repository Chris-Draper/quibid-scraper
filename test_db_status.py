from peewee import * 
# should be able to use "import peewee" but that doesn't work
# I had to pip install PyMySQL to be able to use SQL databases

db = MySQLDatabase(database='chris_quibids_db', host='216.219.81.80', 
        port=3306, user='chris_admin', password='Rhshornet21!!')
db.connect()
print("Connected to db successfully")
db.close()