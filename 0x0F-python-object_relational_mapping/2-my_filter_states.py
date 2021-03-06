#!/usr/bin/python3

"""Takes in an argument and displays all values in the states table"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                               user=argv[1], passwd=argv[2], database=argv[3])
    cur = database.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY states.id ASC"
                .format(argv[4]))
    for row in cur.fetchall():
        if row[1] == argv[4]:
            print(row)
    cur.close()
    database.close()
