# from turtle import screensize
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Laptop(Base):
    
    __tablename__ = "laptop"
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    screen_size = Column(Integer)
    brand = Column(String)
    battery = Column(Integer)
    
if __name__ == '__main__':
      engine = create_engine('sqlite:///mydatabase.sqlite')
      Base.metadata.create_all(engine)