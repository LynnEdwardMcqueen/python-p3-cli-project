from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///recipes.db')
Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer(), primary_key=True)
    recipe_title = Column(String())
    vegetables_and_fruit = Column(Integer())
    breads_and_cereals = Column(Integer())
    dairy = Column(Integer())
    meat = Column(Integer())
    fats_and_sugar = Column(Integer())
    reviews = relationship('Review', backref=backref('game'))
    instructions = relationship('Instruction', backref=backref('recipe'))
    ingredients = relationship('Ingredient', backref=backref('recipe'))

class Instruction(Base):
    __tablename__ = 'instructions'

    id = Column(Integer(), primary_key=True)
    instruction = Column(String())
    recipe_id = Column(Integer(), ForeignKey('recipes.id'))

class Ingredient(Base):

    __tablename__ = 'ingredients'

    id = Column(Integer(), primary_key=True)
    measurement_amount = Column(String())
    measurement_unit = Column(String())
    ingredient = Column(String())
    recipe_id = Column(Integer(), ForeignKey('recipes.id'))



