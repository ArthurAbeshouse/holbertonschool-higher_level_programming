#!/usr/bin/python3
"""Adds San Francisco, California to the database"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username=argv[1],
            password=argv[2],
            db_name=argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    session.add(new_state)
    session.add(new_city)
    session.commit()
    session.close()
