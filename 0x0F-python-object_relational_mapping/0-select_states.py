#!/usr/bin/python3

import MySQLdb
from sys import argv


def get_states():
    ''' Get states from hbtn_0e_0_usa database '''
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
    states = get_states()
