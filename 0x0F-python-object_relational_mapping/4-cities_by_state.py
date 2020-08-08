#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv


def get_data(db):
    ''' Get data from hbtn_0e_4_usa database '''
    try:
        cur = db.cursor()
        cur.execute("SELECT cities.id, cities.name, states.name\
                     FROM cities JOIN states\
                     ON states.id = cities.state_id\
                     ORDER BY id ASC")
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
    cities = get_data(db)
    for city in cities:
        print(city)
