#!/usr/bin/python3
""" script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
from sys import argv


def get_data(db, name):
    ''' Get data from hbtn_0e_0_usa database '''
    try:
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name='{}'\
                     ORDER BY id ASC".format(name))
        state = cur.fetchall()
    except MySQLdb.Error as e:
        print('MySQL Error {}: {}'.format(e.args[0], e.args[1]))
    finally:
        cur.close()
        db.close()
        return(state)


def connect_database(host, port, user, passwd, db):
    ''' Function connect database '''
    db = MySQLdb.connect(host=host,
                         port=port,
                         user=user,
                         passwd=passwd,
                         db=db)
    return(db)


if __name__ == "__main__":
    db = connect_database('localhost', 3306, argv[1], argv[2], argv[3])
    states = get_data(db, argv[4])
    for state in states:
        if state[1] == argv[4]:
            print(state)
