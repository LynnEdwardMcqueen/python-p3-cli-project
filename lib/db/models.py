from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


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
    recipe_is_active = Column(Integer())
    instructions = relationship('Instruction', backref=backref('recipe'))
    ingredients = relationship('Ingredient', backref=backref('recipe'))

    def __repr__(self):
        return f'Recipe (id={self.id}, ' + \
            f'recipe_title = {self.recipe_title}, ' + \
            f'veggies_and_fruit = {self.vegetables_and_fruit}, ' +\
            f'breads = {self.breads_and_cereals}, ' +\
            f'dairy = {self.dairy}, ' +\
            f'meat = {self.meat}, ' +\
            f'fats_and_sugar = {self.fats_and_sugar}, ' +\
            f'recipe_is_active = {self.recipe_is_active}'


            
    

class Instruction(Base):
    __tablename__ = 'instructions'

    id = Column(Integer(), primary_key=True)
    instruction = Column(String())
    recipe_id = Column(Integer(), ForeignKey('recipes.id'))

    def __repr__(self):
        return f'Instruction (id = {self.id})' +\
            f'recipe_id = {self.recipe_id}' +\
            f'instruction = {self.instruction}'

class Ingredient(Base):

    __tablename__ = 'ingredients'

    id = Column(Integer(), primary_key=True)
    measurement_amount = Column(String())
    measurement_unit = Column(String())
    ingredient = Column(String())
    recipe_id = Column(Integer(), ForeignKey('recipes.id'))

    def __repr__(self):
        return f'Ingredient (id = {self.id}) ' +\
            f'recipe_id = {self.recipe_id} ' +\
            f'measurement_amount = {self.measurement_amount} ' +\
            f'measurement_unit = {self.measurement_unit} ' +\
            f'ingredient = {self.ingredient} '




