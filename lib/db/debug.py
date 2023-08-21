#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Recipe, Ingredient, Instruction

if __name__ == '__main__':
    engine = create_engine('sqlite:///recipes.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    recipe1 = Recipe(
        recipe_title = "Chicken Pot Pie",
        vegetables_and_fruit = 1,
        breads_and_cereals = 1,
        dairy = 0,
        meat = 1,
        fats_and_sugar = 1,
        instructions = None,
        ingredients = None,)
    
    session.add(recipe1)
    session.commit()
    import ipdb; ipdb.set_trace()

