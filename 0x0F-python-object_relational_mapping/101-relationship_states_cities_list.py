#!/usr/bin/python3
""" script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""

from sys import argv
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def get_data(engine):
    ''' Get data from database '''
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).order_by(State.id).all()

    return (data, session)


def connect_database(user, passwd, db):
    ''' Connect to database '''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    return (engine)


if __name__ == "__main__":
    engine = connect_database(argv[1], argv[2], argv[3])
    data, session = get_data(engine)

    for state in data:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('{}{}: {}'.format('\t', city.id, city.name))
    session.close()
