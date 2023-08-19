from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///recipes.db')
Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer(), primary_key=True)
    recipe_title = Column(String())
    vegetables_and_fruit = Column(Integer())
    breads_and_cereals = Column(Integer())
    dairy = Column(Integer())
    meat = Column(Integer())
    fats_and_sugar = Column(Integer())



