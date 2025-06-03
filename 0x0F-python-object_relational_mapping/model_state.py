#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create instance of declarative base
Base = declarative_base()

class State(Base):
    """
    State class that inherits from Base
    
    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
    """
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    
if __name__ == "__main__":
    # Create an engine that connects to the database
    engine = create_engine('mysql+pymysql://{}:{}@localhost:3306/{}'
                          .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    
    # Create all tables in the engine
    Base.metadata.create_all(engine)
