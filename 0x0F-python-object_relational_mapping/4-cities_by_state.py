#!/usr/bin/python3

"""Lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                               user=argv[1], passwd=argv[2], database=argv[3])
    cur = database.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
    LEFT JOIN states ON cities.state_id = states.id\
    ORDER BY cities.id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    database.close()
