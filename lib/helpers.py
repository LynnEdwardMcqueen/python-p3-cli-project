from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Recipe, Ingredient, Instruction 
import ipdb



class Helper:

    def __init__(self):
        self.engine = create_engine('sqlite:///db/recipes.db')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()


    def get_matching_ingredient(self, search_ingredient):
        matching_recipes = self.session.query(Ingredient.recipe_id).filter(Ingredient.ingredient.like(f'%{search_ingredient}%')).all()

        # There is a possibility that some ingredients are used multiple times in a recipe.  Putting the values into a set
        # will eliminate redundant values.
        matching_recipe_set = set(matching_recipes)
        print(f"The matching recipes are {matching_recipe_set}")
        # Now that any redundant recipes are eliminated, remake the list and sort it.
        matching_recipes = list(matching_recipe_set)
        matching_recipes.sort()

    #
    # This routine takes the recipe_ids and returns a list of all the ingredients associated with the recipes.
    # The list is in alphabetical order.  PLEASE NOTE!!!!  As a side effect of database conventions, all
    # elements of the list are single element tuples that have a string containing an individual ingredient.
    #
    def get_shopping_list(self, recipe_ids):
        shopping_list = []

        for recipe_id in recipe_ids:
            recipe_list = self.session.query(Ingredient.ingredient).filter(Ingredient.recipe_id == recipe_id).all()
            shopping_list = [*shopping_list, *recipe_list]
        shopping_list.sort()
        
        return(shopping_list)
        
  
    def get_selected_recipes_list(self, recipe_list):
        recipe_list_data = []
        for recipe_index in recipe_list:
            recipe_info = self.session.query(Recipe.id, Recipe.recipe_title).filter(Recipe.id == recipe_index).all()
            recipe_list_data = [*recipe_list_data, *recipe_info]
            
        return recipe_list_data

             
    def get_recipe_list(self, alphabetized = False):
      
        # Return the id and recipe_title information.  
        if alphabetized == False:
            order_criteria = Recipe.id
        else:
            order_criteria = Recipe.recipe_title

        # We will return a list of tuples.  Each tuple contains the recipe id and the recipe title.
        recipe_title_list = self.session.query(Recipe.id, Recipe.recipe_title).order_by(order_criteria).all()
        
        return(recipe_title_list)
    
    #
    # This method assembles the requested recipe information:  Recipe Title & Food Pyramid Info, Ingredients and Instructions.  It returns
    # a data structure that is a tuple that contains 3 elements.  The first is the recipe information with the title and food pyrmid info, the second
    # contains the instructions, and finally the 3 contains all the ingredient information
    #
    # ( [id, recipe_title, recipe_food_pyramid_info)],
    #   [(ingredient_info_1), (ingredient_info_2),...(ingredient_info_n)],
    #   [(instruction_1,), (instruction_2,),...(instruction_n,)]
    # )
    def get_selected_recipe(self, recipe_id):
        recipe_info = self.session\
            .query(Recipe.recipe_title, Recipe.vegetables_and_fruit, Recipe.breads_and_cereals, Recipe.dairy, Recipe.meat, Recipe.fats_and_sugar )\
            .filter(Recipe.id == recipe_id).all()
        
        instruction_info = self.session.query(Instruction.instruction).filter(Instruction.recipe_id == recipe_id).all()
        ingredient_info = self.session.query(Ingredient.measurement_amount, Ingredient.measurement_unit, Ingredient.ingredient)\
            .filter(Ingredient.recipe_id == recipe_id).all()
     
        # The recipe_info has a single tuple embedded in a list (i.e. [(recipe_title, food_pyramid_info1,...)]).  Extract the tuple from the 
        # list and make that the 0th element of the return tuple.  In short, that's why there is recipe_info[0] instead of recipe_info
        return_info = (recipe_info[0], ingredient_info, instruction_info)



        return((recipe_info[0], ingredient_info, instruction_info))
