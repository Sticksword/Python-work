__author__ = 'Michael'

import csv
import sqlite3

database = 'crawled.db'  # global variable to hold database name

def write_one_to_db_version4(dept, courseNum, courseType, professor):
    """ demos writing one record to the DB, uses parameter substitution (solid way to do this)"""
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        sql_cmd = "insert into coursedata values(?, ?, 9000, ? , 20, 20, ?)"
        cur.execute(sql_cmd, (dept, courseNum, courseType, professor)) # use ? in command string and a tuple to fill in each ?
        # this is nice, clean, simple. Don't have to remember quotes.  Also, avoids security risk!

def read_line_from():
    """
    reads from csv and puts into database
    """
    f = open('seas-courses-5years.csv', 'rU')
    for line in f:
        words = line.split(',')
        write_one_to_db_version4(words[0], words[1], words[3], words[6])

def read_from_database():
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        sql_cmd = "SELECT * FROM coursedata"
        cur.execute(sql_cmd)
        rows = cur.fetchall()
        for row in rows:
            print row

if __name__ == '__main__':
    read_line_from()
    read_from_database()