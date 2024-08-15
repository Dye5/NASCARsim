import sqlite3
import random
from textwrap import shorten

con = sqlite3.connect('tutorial.db')
cur = con.cursor()
cur2 = con.cursor()

p = 0
while p < 1:
    tracktype = input("What type of track is this?\n [A] Short Track\n [B] Intermediate\n [C] Superspeedway\n [D] Road Course\n")
    if tracktype =="A":
        track = "shrt"
        p = p + 1
    elif tracktype =="B":
        track = "med"
        p = p + 1
    elif tracktype =="C":
        track = "ss"
        p = p + 1
    elif tracktype =="D":
        track = "road"
        p = p + 1
    else:
        print("Input not recognized. Please try again")

def qualitime(drivername):

    if track=="shrt":
        cur.execute("SELECT shrt FROM driver WHERE name = ?", (drivername, ))
        rows = cur.fetchall()
        for row in rows:
            shrt = row[0]
        cur.execute("SELECT ovr FROM driver WHERE name = ?", (drivername, ))
        rows = cur.fetchall()
        for row in rows:
            ovr = row[0]
        cur.execute("SELECT quali FROM driver WHERE name = ?", (drivername,))
        rows = cur.fetchall()
        for row in rows:
            quali = row[0]
        qualiskill = ((shrt + ovr + quali))
        qualifier1 = random.randint(50, 90)
        qualifier2 = random.randint(50, 90)
        qualifier3 = random.randint(50, 90)
        totalqual = qualiskill + qualifier1 + qualifier2 + qualifier3
        cur.execute("UPDATE driver SET qualitime = ? WHERE name = ?", (totalqual, drivername))
        return
    elif track=="med":
        cur.execute("SELECT med FROM driver WHERE name = ?", (drivername,))
        rows = cur.fetchall()
        for row in rows:
            shrt = row[0]
        cur.execute("SELECT ovr FROM driver WHERE name = ?", (drivername,))
        rows = cur.fetchall()
        for row in rows:
            ovr = row[0]
        cur.execute("SELECT quali FROM driver WHERE name = ?", (drivername,))
        rows = cur.fetchall()
        for row in rows:
            quali = row[0]
        qualiskill = ((shrt + ovr + quali))
        qualifier1 = random.randint(50, 90)
        qualifier2 = random.randint(50, 90)
        qualifier3 = random.randint(50, 90)
        totalqual = qualiskill + qualifier1 + qualifier2 + qualifier3
        cur.execute("UPDATE driver SET qualitime = ? WHERE name = ?", (totalqual, drivername))
        return
    elif track=="ss":
        cur.execute("SELECT ss FROM driver WHERE name = ?", (drivername,))
        rows = cur.fetchall()
        for row in rows:
            shrt = row[0]
        cur.execute("SELECT ovr FROM driver WHERE name = ?", (drivername,))
        rows = cur.fetchall()
        for row in rows:
            ovr = row[0]
        cur.execute("SELECT quali FROM driver WHERE name = ?", (drivername,))
        rows = cur.fetchall()
        for row in rows:
            quali = row[0]
        qualiskill = ((shrt + ovr + quali))
        qualifier1 = random.randint(50, 90)
        qualifier2 = random.randint(50, 90)
        qualifier3 = random.randint(50, 90)
        totalqual = qualiskill + qualifier1 + qualifier2 + qualifier3
        cur.execute("UPDATE driver SET qualitime = ? WHERE name = ?", (totalqual, drivername))
        return
    elif track=="road":
        cur.execute("SELECT road FROM driver WHERE name = ?", (drivername,))
        rows = cur.fetchall()
        for row in rows:
            shrt = row[0]
        cur.execute("SELECT ovr FROM driver WHERE name = ?", (drivername,))
        rows = cur.fetchall()
        for row in rows:
            ovr = row[0]
        cur.execute("SELECT quali FROM driver WHERE name = ?", (drivername,))
        rows = cur.fetchall()
        for row in rows:
            quali = row[0]
        qualiskill = ((shrt + ovr + quali))
        qualifier1 = random.randint(50, 90)
        qualifier2 = random.randint(50, 90)
        qualifier3 = random.randint(50, 90)
        totalqual = qualiskill + qualifier1 + qualifier2 + qualifier3
        cur.execute("UPDATE driver SET qualitime = ? WHERE name = ?", (totalqual, drivername))
        return


pos = 1

def updatequalipos(d_name, qualiposition):
    cur.execute("UPDATE driver SET qualipos = ? WHERE name = ?", (qualiposition, d_name))
    return
def updateracepos(d_name, qualiposition):
    cur.execute("UPDATE driver SET racepos = ? WHERE name = ?", (qualiposition, d_name))
    return



while pos <=6:
    cur.execute("SELECT name FROM driver WHERE standing = ?", (pos,))
    rows = cur.fetchall()
    for row in rows:
        qualifier = (row[0])
        qualitime(qualifier)

    pos = pos + 1


cur.execute("SELECT name FROM driver ORDER BY qualitime DESC")
rows = cur.fetchall()
i = 1
for row in rows:
    d_name = row[0]
    updatequalipos(d_name, i)
    updateracepos(d_name, i)
    i = i + 1




cur.execute("SELECT name, num, qualipos, qualitime FROM driver ORDER BY qualipos")
rows = cur.fetchall()
for row in rows:
    print("Name:", row[0], "Number:", row[1], "Qualifying Position:", row[2], "Speed:", row[3], " \n")

#grid = input("Would you like to see the starting grid?\n[Y] Yes\n[N] No\n")
y = 0
while y < 1:
    grid = input("Would you like to see the starting grid?\n[Y] Yes\n[N] No\n")
    if grid =="Y":
        cur.execute("SELECT num FROM driver ORDER BY racepos")
        rows = cur.fetchall()
        t = 0
        gridpos = [None] * 6
        for row in rows:
            gridpos[t] = row[0]
            t = t + 1
        print("Inside  ", "Outside ", "\n", gridpos[0], "     ", gridpos[1], "\n", gridpos[2], "     ", gridpos[3], "\n", gridpos[4], "     ", gridpos[5], "\n")
        y = y + 1
    elif grid =="N":
        print("Qualifying Complete")
        y = y + 1
    else:
        print("Input not recognized")



con.close()
