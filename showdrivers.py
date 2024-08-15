import sqlite3

conn = sqlite3.connect('tutorial.db')
print("Opened database successfully")

#conn.execute("DELETE from driver where num = 11")
#conn.commit()
print("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT num, name, team, mfr from driver")
for row in cursor:
   print("NUM = ", row[0])
   print("NAME = ", row[1])
   print("TEAM = ", row[2])
   print("MANUFACTURER = ", row[3], "\n")

print("Operation done successfully")
conn.close()

