#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)

'''
The engine is "home base" for the database- everything on the database side and the Python side must pass through the engine for the process to count. Here, we're pointing to a local sqlite file where our tables will be created.

The create_all() command on the next line tells the engine that any models that were created using Base as a parent should be used to create tables.
'''