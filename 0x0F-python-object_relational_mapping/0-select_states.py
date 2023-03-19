#!/usr/bin/python3
"""List all states from a given db sorted in ascending order by id
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    allStates = cur.fetchall()

    for state in allStates:
        print(state)

    cur.close()
    db.close()

  """
  db = MySQLdb.connect(host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
  """
