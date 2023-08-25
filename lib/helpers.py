from sqlalchemy import create_engine, func, column
from sqlalchemy.orm import sessionmaker
from db.models import Recipe, Ingredient, Instruction 
import ipdb



class Helper:

    def __init__(self):
        # Super important state information to set up SQLAlchemy.  The engine must be created, and then the session bound to
        # the engine.  This will be used to interface with the recipes database.
        self.engine = create_engine('sqlite:///db/recipes.db')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        # This information is needed in multiple parts of the code.  This is the single source of truth.
        self.food_pyramid_entries = ["vegetables_and_fruit", "breads_and_cereals", "dairy", "meat", "fats_and_sugar"]

    def add_recipe(self, recipe_title, veggies_and_fruit, breads, dairy,meat,fats_and_sugar, ingredients, instructions):


        new_recipe = Recipe(recipe_title = recipe_title,
            vegetables_and_fruit = veggies_and_fruit,
            breads_and_cereals = breads,
            dairy = dairy,
            meat = meat,
            fats_and_sugar = fats_and_sugar,
            recipe_is_active = True,
            )

   

        self.session.add(new_recipe)
        self.session.commit()

        print(f"The new recipe (post session!) is {new_recipe}")

        # Update the Ingredient table with the ingredients from the new recipe, using
        # the new_recipe.id to tie the information back to the new_recipe entry in
        # the Recipe table.
        for ingredient in ingredients:
            new_ingredient = Ingredient(measurement_amount = ingredient[0],
                measurement_unit = ingredient[1],
                ingredient = ingredient[2],
                recipe_id = new_recipe.id)
        
            self.session.add(new_ingredient)
            self.session.commit()
            print(f"new_ingredient = {new_ingredient}")

        # Update the Instruction table with the instructions from the new recipe.
        # Remember that new_recipe.id is the recipe_id for each new instruction entry
        # in the Instruction table.
        for instruction in instructions:
            new_instruction = Instruction(instruction = instruction,
                recipe_id = new_recipe.id)
            self.session.add(new_instruction)
            self.session.commit()
            print(f"new instruction = {new_instruction}")

    def change_recipe_name(self, recipe_id, new_title):
        # This will be a read/modify/write operation, so first read the recipe corresponding to recipe_id
        print(f"recipe_id = {recipe_id} and title = {new_title}")
        # Note that the final method is "first" not "all".  We only need 1 recipe!
        recipe = self.session.query(Recipe).filter(Recipe.id == recipe_id).first()
        recipe.recipe_title = new_title

        # Now that the recipe record has the updated title, commit it to the Recipe table.
        self.session.commit()

    def delete_recipe(self, recipe_id):
        # INCREDIBLY IMPORTANT!!!! You must delete the foreign_key records first before deleting the
        # parent record.  

        delete_ingredients = self.session.query(Ingredient).filter(Ingredient.recipe_id == recipe_id).all()
        print(delete_ingredients)
        for delete_ingredient in delete_ingredients:
            self.session.delete(delete_ingredient)
        self.session.commit()
    
        delete_instructions = self.session.query(Instruction).filter(Instruction.recipe_id == recipe_id).all()
        print(delete_instructions)
        for delete_instruction in delete_instructions:
            self.session.delete(delete_instruction)
        self.session.commit()

        # NOW!! Delete the parent record now that the child records are gone!
        delete_record = self.session.query(Recipe).filter(Recipe.id == recipe_id).first()
        self.session.delete(delete_record)
        self.session.commit()





    def get_pyramid_information(self, recipe_list):
        food_pyramid_dictionary = {}

        # Initialize all category entries to 0
        for category in self.food_pyramid_entries:
            food_pyramid_dictionary[category] = 0
        
        for recipe_id in recipe_list:
            food_results = self.session.query(Recipe.vegetables_and_fruit, Recipe.breads_and_cereals,Recipe.dairy, Recipe.meat, Recipe.fats_and_sugar)\
                .filter(Recipe.id == recipe_id).all()
            
           
            # Update the food pyramid dictionary.  The database returns a list of tuples.  Since the tuple with the column results is the only item
            # in the list, food_results[0][i] is used to retrieve each individual result.
            i = 0
            for category in self.food_pyramid_entries:
                food_pyramid_dictionary[category] += food_results[0][i]
                i += 1
        return food_pyramid_dictionary


    def get_recipe_matching_ingredient(self, search_ingredient):
        matching_recipes = self.session.query(Ingredient.recipe_id).filter(Ingredient.ingredient.like(f'%{search_ingredient}%')).all()

        # There is a possibility that some ingredients are used multiple times in a recipe.  Putting the values into a set
        # will eliminate redundant values.
        matching_recipe_set = set(matching_recipes)
        # Now that any redundant recipes are eliminated, remake the list and sort it.
        matching_recipes = list(matching_recipe_set)
        # The database returns everything as tuples.  Extract the recipe_id's and make a new list of them
        matching_recipes = [recipe[0] for recipe in matching_recipes]
        matching_recipes.sort()
        return_value =self.get_selected_recipes_list(matching_recipes)
        return(return_value)

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
        return((recipe_info[0], ingredient_info, instruction_info))
