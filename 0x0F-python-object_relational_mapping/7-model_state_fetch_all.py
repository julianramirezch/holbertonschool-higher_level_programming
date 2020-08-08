#!/usr/bin/python3
""" script that lists all State objects from the database hbtn_0e_6_usa
    using SQLAlchemy """

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def get_data(engine):
    ''' Get data from database '''
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_data = session.query(State).order_by(State.id).all()
    for state in states_data:
        print('{}: {}'.format(state.id, state.name))

    session.close()


def connect_database(user, passwd, db):
    ''' Connect to database '''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    return (engine)


if __name__ == "__main__":
    engine = connect_database(argv[1], argv[2], argv[3])
    get_data(engine)
