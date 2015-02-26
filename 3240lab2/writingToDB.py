__author__ = 'Michael'

import sqlite3
import sys


cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)


con = sqlite3.connect('test.db')

with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)

# one method of reaching into a database and printing its contents
# with con:
#     cur = con.cursor()
#     sql_cmd = "SELECT * FROM Cars"
#     cur.execute(sql_cmd)
#     rows = cur.fetchall()
#     for row in rows:
#         print row

#--------------------------------------------------------------------
# with con:
# # data is in form of dictionaries, can refer to the data by their column names
# # this is a dictionary cursor
#     con.row_factory = sqlite3.Row
#
#     cur = con.cursor()
#     cur.execute("SELECT * FROM Cars")
#
#     rows = cur.fetchall()
#
#     for row in rows:
#         print "%s %s %s" % (row["Id"], row["Name"], row["Price"])

#------------------------------------------------------------------
with con:
# normally this would give us a tuple of tuples as the data
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")
    while True:
        row = cur.fetchone()
        if row == None:
            break

        print row[0], row[1], row[2]
    uId = 1
    uPrice = 62300
# ? marks as parameterized query
    cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId))
    cur.execute("SELECT * FROM Cars WHERE Id=1")

    row = cur.fetchone()
    print row
    #print "Number of rows updated: %d" % cur.rowcount


# named placeholders as parameterized query
    cur.execute("SELECT Name, Price FROM Cars WHERE Id=:Id",
        {"Id": uId})
    con.commit()

    row = cur.fetchone()
    print row[0], row[1]

# retrieving and printing the database
    cur.execute('SELECT * FROM Cars')
    col_names = [cn[0] for cn in cur.description]

    rows = cur.fetchall()

    print "%s %-10s %s" % (col_names[0], col_names[1], col_names[2])

# print all the tables in database
    for row in rows:
        print "%2s %-10s %s" % row

    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")

    rows = cur.fetchall()

    for row in rows:
        print row[0]

#-------------------------------------------------------------------
# one way of inserting into a database
# with con:
#
#     cur = con.cursor()
#     cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
#     cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
#     cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
#     cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
#     cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
#     cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
#     cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
#     cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
#     cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")