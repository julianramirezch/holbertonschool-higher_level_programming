#!/usr/bin/python3

import MySQLdb
from sys import argv


def get_states(db):
    ''' Get states from hbtn_0e_0_usa database '''
        cur = db.cursor()
        cur.execute("""SELECT * FROM states ORDER BY id ASC""")
        states = cur.fetchall()
        cur.close()
        db.close()
        return(states)


def connect_database(host, port, user, passwd, db):
    ''' Function connect database '''
    db = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db)
    return(db)


if __name__ == "__main__":
    db = connect_database('localhost', 3306, argv[1], argv[2], argv[3])
    states = get_states(db)
    for state in states:
        print(state)
