#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Recipe, Ingredient, Instruction

if __name__ == '__main__':

    engine = create_engine('sqlite:///recipes.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    ingredient_list = ( (2, "C", "diced peeled potatoes"),
    ("1-3/4", "C", "sliced carrots"),
    ("1", "C", "butter cubed"),
    ("2/3", "C", "chopped onion"),
    ("1", "C", "all-purpose flour"),
    ("1-3/4", "t", "salt"),
    ("1", "t", "dried thyme"),
    ("3/4", "t", "pepper"),
    ("3", "C", "chicken broth"),
    ("1-1/2", "C", "whole milk"),
    ("4", "C", "cubed cooked chicken"),
    ("1", "C", "frozen peas"),
    ("1", "C", "frozen corn"),
    ("4",None ,"sheets refrigerated pie crust")
    )


    first_recipe = session.query(Recipe).first()
    print (first_recipe)
    print (first_recipe.id)

    for ingredient in ingredient_list:
        ingredient_row = Ingredient ( 
            recipe_id = first_recipe.id,
            measurement_amount = ingredient[0],
            measurement_unit = ingredient[1],
            ingredient = ingredient[2],
        )

        session.add(ingredient_row)
        session.commit()
        print(ingredient_row)
        



     
    import ipdb; ipdb.set_trace()
    
    session.add(recipe1)
    session.commit()
   

