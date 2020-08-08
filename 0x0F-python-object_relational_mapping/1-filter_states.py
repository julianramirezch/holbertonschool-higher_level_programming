#!/usr/bin/python3
""" script that lists all states with a name starting with N (upper N) from
    the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv


def get_data(db):
    ''' Get data from hbtn_0e_0_usa database '''
    try:
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%'\
                     ORDER BY id ASC")
        states = cur.fetchall()
    except MySQLdb.Error as e:
        print('MySQL Error {}: {}'.format(e.args[0], e.args[1]))
    finally:
        cur.close()
        db.close()
        return(states)


def connect_database(host, port, user, passwd, db):
    ''' Connect database '''
    db = MySQLdb.connect(host=host,
                         port=port,
                         user=user,
                         passwd=passwd,
                         db=db)
    return db


if __name__ == "__main__":
    db = connect_database('localhost', 3306, argv[1], argv[2], argv[3])
    states = get_data(db)
    for state in states:
        print(state)
