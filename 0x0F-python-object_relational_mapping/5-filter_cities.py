#!/usr/bin/python3
""" script that takes in the name of a state as an argument and lists all
    cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv


def get_data(db, state):
    ''' Get data from hbtn_0e_4_usa database '''
    try:
        cur = db.cursor()
        cur.execute("SELECT cities.name FROM cities JOIN states\
                     ON cities.state_id=states.id\
                     WHERE states.name=%s ORDER BY cities.id ASC", (state, ))
        cities = cur.fetchall()
    except MySQLdb.Error as e:
        print('MySQL Error {}: {}'.format(e.args[0], e.args[1]))
    finally:
        cur.close()
        db.close()
        return(cities)


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
    cities = get_data(db, argv[4])
    state_cities = []
    for idx, city in enumerate(cities):
        state_cities.append(cities[idx][0])
    print(', '.join(state_cities))
