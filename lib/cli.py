from cmdprocessor import CmdProcessor
import click
from helpers import display_recipe, display_recipe_list, display_shopping_list,get_new_recipe_ingredients, get_new_recipe_instructions


cmd_processor = CmdProcessor()

@click.group()
def cli():
    pass    


@click.option("-j", "--instruction", type = str, multiple = True)
@click.option("-t", "--title", required = True, prompt = True)
@click.option("-v", "--veggies_and_fruits", type = int, default = 0)
@click.option("-m", "--meat", type = int, default = 0)
@click.option("-d", "--dairy", type = int, default = 0)
@click.option("-b", "--bread", type = int, default = 0)
@click.option("-s", "--sugars_and_fats", type = int, default = 0)
@click.option("-i", "--ingredient", type = (str, str, str), multiple = True, help = "TEXT 1 = Amount, examples are 1-5/8, .75.  TEXT 2 = unit, exampes are tsp, cup, oz.  TEXT 3 = ingredient")
@cli.command()
def addrecipe(title, veggies_and_fruits, meat, dairy, bread, sugars_and_fats, ingredient, instruction):
    """
    Adds a new recipe to the list.  Includes:  Recipe title, food pyramid info, ingredients, and instructions.
    """

    ingredient_list = get_new_recipe_ingredients(ingredient)

    instruction_list = get_new_recipe_instructions(instruction)

    cmd_processor.add_recipe(title, veggies_and_fruits, meat, dairy, bread, sugars_and_fats, ingredient_list, instruction)

    


@click.option("-r", "--recipe_id", required = True, type = int, help="Numerical Id of the recipe")
@click.option("-t", "--title", required = True, help="New title for the recipe")
@cli.command()
def changerecipetitle(recipe_id, title):
    """Changes the name/title of a recipe."""
    cmd_processor.change_recipe_name(recipe_id, title)

@click.argument
@click.argument("recipe_ids", nargs = -1)
@cli.command()
def createshoppinglist(recipe_ids):
    """Creates a shopping list from a list of recipe ids

    RECIPE_IDS is a list of recipe indices from which to build the list. 
    """
    # The arguments are sent in a tuple as strings.  Need to be converted
    # to ints
    shopping_ids = [int(recipe_id) for recipe_id in recipe_ids]
    shopping_list = cmd_processor.get_shopping_list(shopping_ids)
    recipes_list = cmd_processor.get_selected_recipes_list(shopping_ids)
    display_shopping_list(recipes_list, shopping_list)

@click.option("-i", "--index", type = int, required=True, help="Numerical index of the recipe you wish to delete")
@cli.command()
def deleterecipe(index):
    """Deletes a recipe from the database
    
    """
    cmd_processor.delete_recipe(index)


@click.option("-i", "index", required=True, help="Numerical index of the recipe you wish to display" )
@cli.command()
def displayrecipe(index):
    """Takes a recipe id and displays the recipe details
    
    RECIPE_ID is the index of the recipe to display.
    """
    # Click sends all arguments as strings.  The recipe_id needs to be converted to
    # integers
    recipe_info = cmd_processor.get_selected_recipe(int(recipe_id))
    display_recipe(recipe_info)

@click.option("-a", "--alpha", is_flag = True, show_default = True, default = 0, help = "Alphabetize the list")
@cli.command()
def listrecipes(alpha):
    """Displays the recipe ids and titles"""
    recipe_list = cmd_processor.get_recipe_list(alpha)
    display_recipe_list(recipe_list)

@click.argument("ingredient", nargs = 1)
@cli.command()
def matchingingredient(ingredient):
    """Displays a list of recipes containing an ingredient

    INGREDIENT is the search ingredient.  
    """
    recipe_list = cmd_processor.get_recipe_matching_ingredient(ingredient)
    click.echo(f"Recipes with {ingredient} as an ingredient: ")
    display_recipe_list(recipe_list)

@click.argument("recipe_list", nargs = -1)
@cli.command()
def showpyramidinfo(recipe_list):
    """Returns the nutrition pyramid info for a recipe list
    
    RECIPE_LIST contains the numerical indices of the recipes
    """
    recipe_list = [int(recipe) for recipe in recipe_list]
    click.echo("Food Pyramid Info For:")
    recipe_info = cmd_processor.get_selected_recipes_list(recipe_list)
    display_recipe_list(recipe_info)
    
    click.echo("\nFood Pyramid Data:")
    pyramid_result_dictionary = cmd_processor.get_pyramid_information(recipe_list)
    for category in cmd_processor.food_pyramid_entries:
        click.echo(f"{category} - {pyramid_result_dictionary[category]}")


if __name__ == "__main__":
    cli()