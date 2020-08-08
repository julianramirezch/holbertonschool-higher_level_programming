#!/usr/bin/python3


def get_states(db):
    try:
        cur = db.cursor()
        cur.execute("""SELECT * FROM states ORDER BY id ASC""")
        states = cur.fetchall()
    except MySQLdb.Error as e:
        print('MySQL Error {}: {}'.format(e.args[0], e.args[1]))
    finally:
        cur.close()
        db.close()
        return(states)


def connect_database(host, port, user, passwd, db):
    db = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db)
    return(db)


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = connect_database('localhost', 3306, argv[1], argv[2], argv[3])
    states = get_states(db)
    for state in states:
        print(state)
