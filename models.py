from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from database import Base


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    track = Column(String, default=True)

#Person validator
class Item(BaseModel):
    name: str 
    age: int
    track: str 
