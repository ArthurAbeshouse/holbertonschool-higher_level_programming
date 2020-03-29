#!/usr/bin/python3
"""Prints the State object with the name passed as
argument from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name == argv[4]).all()
    if states:
        print("{}".format(states[0].id))
    else:
        print("Not found")
    session.close()
