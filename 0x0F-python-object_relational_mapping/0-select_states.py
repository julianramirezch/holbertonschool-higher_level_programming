#!/usr/bin/python3

import MySQLdb
from sys import argv


def get_states(db):
    ''' Get states from hbtn_0e_0_usa database '''
    db = connect_database('localhost', 3306, argv[1], argv[2], argv[3])
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    try:
        cur = db.cursor()
        cur.execute('SELECT * FROM states ORDER BY id ASC')
        states = cur.fetchall()
    except MySQLdb.Error as e:
        print('MySQL Error {}: {}'.format(e.args[0], e.args[1]))
    finally:
        cur.close()
        db.close()
    for state in states:
        print(state)


if __name__ == "__main__":
    states = get_states(db)
