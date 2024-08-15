import sqlite3


con = sqlite3.connect("tutorial.db")

cur = con.cursor()

print(con.total_changes)

cur.execute("CREATE TABLE IF NOT EXISTS driver (num, name, team, mfr, standing, qualipos, qualitime, racepos, ovr, quali, ss, med, shrt, road, tire, restart)")

cur.execute("INSERT INTO driver VALUES (5, 'Kyle Larson', 'Hendrick Motorsports', 'Chevrolet', 1, 1, 1, 1, 95, 93, 72, 96, 90, 88, 90, 92)")
cur.execute("INSERT INTO driver VALUES (9, 'Chase Elliott', 'Hendrick Motorsports', 'Chevrolet', 3, 3, 3, 3, 89, 86, 87, 88, 83, 92, 87, 83)")
cur.execute("INSERT INTO driver VALUES (11, 'Denny Hamlin', 'Joe Gibbs Racing', 'Toyota', 2, 2, 2, 2, 94, 93, 90, 94, 89, 75, 94, 93)")
cur.execute("INSERT INTO driver VALUES (22, 'Joey Logano', 'Team Penske', 'Ford', 5, 5, 5, 5, 85, 86, 84, 88, 90, 80, 84, 90)")
cur.execute("INSERT INTO driver VALUES (45, 'Tyler Reddick', '23XI Racing', 'Toyota', 4, 4, 4, 4, 84, 90, 85, 90, 79, 92, 81, 83)")
cur.execute("INSERT INTO driver VALUES (21, 'Harrison Burton', 'Wood Brothers Racing', 'Ford', 6, 6, 6, 6, 60, 62, 65, 58, 57, 59, 60, 62)")


con.commit()
con.close()






