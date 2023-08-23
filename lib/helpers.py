from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Recipe, Ingredient, Instruction 
import ipdb



class Helper:
    def get_recipe_list(alphabetized = False):
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
    
    #
    # This method assembles the requested recipe information:  Recipe Title & Food Pyramid Info, Ingredients and Instructions.  It returns
    # a data structure that is a tuple that contains 3 elements.  The first is the recipe information with the title and food pyrmid info, the second
    # contains the instructions, and finally the 3 contains all the ingredient information
    #
    # ( [id, recipe_title, recipe_food_pyramid_info)],
    #   [(instruction_1,), (instruction_2,),...(instruction_n,)),
    #   [(ingredient_info_1), (ingredient_info_2),...(ingredient_info_n)] )
    # )
    def get_selected_recipe(recipe_id):
        engine = create_engine('sqlite:///db/recipes.db')
        Session = sessionmaker(bind=engine)
        session = Session()

        recipe_info = session\
            .query(Recipe.recipe_title, Recipe.vegetables_and_fruit, Recipe.breads_and_cereals, Recipe.dairy, Recipe.meat, Recipe.fats_and_sugar )\
            .filter(Recipe.id == recipe_id).all()
        print(recipe_info)
        instruction_info = session.query(Instruction.instruction).filter(Instruction.recipe_id == recipe_id).all()
        print(instruction_info)
        ingredient_info = session.query(Ingredient.measurement_amount, Ingredient.measurement_unit, Ingredient.ingredient).filter(Ingredient.recipe_id == recipe_id).all()
        print(ingredient_info)
