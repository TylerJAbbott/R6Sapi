#!/usr/bin/env python

import MySQLdb as db

HOST = "myphpadmin.cbx0wnf0tlqu.us-east-1.rds.amazonaws.com"
PORT = "3306"
USER = "tyler1"
PASSWORD = "Chandra66"
DB = "R6S Leaderboards"

try:
    connection = db.Connection(host=HOSt, port=PORT, user=USER, passwd=PASSWORD, db=DB)
    dbhandler = connection.cursor()
    dbhandler.execute("SELECT * from Leaderboards")
    result = dbhandler.fetchall()
    for item in result:
            print item

    finally:
        connection.close()
