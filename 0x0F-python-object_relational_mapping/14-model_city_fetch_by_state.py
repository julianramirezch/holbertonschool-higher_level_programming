#!/usr/bin/python3
""" script that prints all City objects from the database hbtn_0e_14_usa
    using SQLAlchemy """

from sys import argv
from model_city import Base, City
from model_state import State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def get_data(engine):
    ''' Get data from database '''
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(City, State).filter(City.state_id == State.id).\
        order_by(City.id).all()
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
    for city in data:
        print('{}: ({}) {}'.format(city[1].name, city[0].id, city[0].name))
