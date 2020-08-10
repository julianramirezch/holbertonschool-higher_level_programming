#!/usr/bin/python3
""" script that lists all City objects from the database hbtn_0e_101_usa"""

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

    data = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()
    session.close()

    return (data)


def connect_database(user, passwd, db):
    ''' Connect to database '''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    return (engine)


if __name__ == "__main__":
    engine = connect_database(argv[1], argv[2], argv[3])
    data = get_data(engine)
    for item in data:
        print('{}: {} -> {}'.format(item[0].id, item[0].name, item[1].name))
