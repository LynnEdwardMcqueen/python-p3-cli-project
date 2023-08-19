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


