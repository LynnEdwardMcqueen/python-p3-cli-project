from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Recipe, Ingredient, Instruction 
import ipdb



class Helper:
    def get_recipe_list(alphabetized = False):
        print ('sqlite:///db/recipes.db')
        engine = create_engine('sqlite:///db/recipes.db')
        Session = sessionmaker(bind=engine)
        session = Session()
       
        # Return the id and recipe_title information.  
        if alphabetized == False:
            order_criteria = Recipe.id
        else:
            order_criteria = Recipe.recipe_title

        # We will return a list of tuples.  Each tuple contains the recipe id and the recipe title.
        recipe_title_list = session.query(Recipe.id, Recipe.recipe_title).order_by(order_criteria).all()
        
        return(recipe_title_list)