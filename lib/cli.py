from helpers import Helper
import click

@click.group()
def cli():
    pass    

@click.argument("recipe_ids", nargs = -1)
@cli.command()
def createshoppinglist(recipe_ids):
    # The arguments are sent in a tuple as strings.  Need to be converted
    # to ints
    shopping_ids = [int(recipe_id) for recipe_id in recipe_ids]
    shopping_list = Helper.get_shopping_list(shopping_ids)
    recipes_list = Helper.get_selected_recipes_list(shopping_ids)
    display_shopping_list(recipes_list, shopping_list)


@click.argument("recipe_id", nargs = 1)
@cli.command()
def displayrecipe(recipe_id):
    
    # Click sends all arguments as strings.  The recipe_id needs to be converted to
    # integers
    recipe_info = Helper.get_selected_recipe(int(recipe_id))
    display_recipe(recipe_info)

@click.option("-a", "--alpha", is_flag = True, show_default = True, default = 0)
@cli.command()
def listrecipes(alpha):
    recipe_list = Helper.get_recipe_list(alpha)
    display_recipe_list(recipe_list)



def display_recipe(recipe_info):
    # Print the recipe title
    click.echo(f"Recipe Title:  {recipe_info[0][0]}")
    click.echo("\nIngredients")
    display_recipe_ingredients(recipe_info[1])
    click.echo("\nInstructions")
    display_recipe_instructions(recipe_info[2])

#
# The ingredients_info is a data structure that is a list of tuples containing the ingredient information.
# [(amount, mesurement_unit, ingredient),...].  The amount and measurement unit are right justified in the
# leftmost 9 columns of the display (including a space pad for the ingredient)
#
# The format accomodates non-unit ingredients.  For example, if the recipe calls for 5 eggs,then
#   ingredient_info[0] == 5, ingredient_info[1] == None, ingredient_info[2] == "eggs"
# In this scenario, there is nothing in the 9 columns of measurement info, and the amount is joined with the
# ingredient
def display_recipe_ingredients(ingredients_info):
    for ingredient in ingredients_info:
    
        if ingredient[1] == None:
            ingredient_string = " "*9 + ingredient[0] + " " + ingredient[2]
        else:
            ingredient_string = ("%9s" % (ingredient[0] + " " + ingredient[1] + " ")) + ingredient[2]
        click.echo(ingredient_string)

#
# instruction_info is a list of single element tuples that contain the step by step instructins for the recipe.
# [(instruction1,), (instruction2,), ... (instructionn,)]
def display_recipe_instructions(instruction_info):
    instruction_number = 1
    for instruction in instruction_info:
        # instruction is a single element tuple, so display instruction[0]
        click.echo(f"{instruction_number}.  {instruction[0]}")
        instruction_number += 1
        
        
def display_recipe_list(recipe_list):
    for recipe_item in recipe_list:
        display_string = "  ".join( (str(recipe_item[0]),recipe_item[1]) )
        click.echo(display_string)

def display_shopping_list(recipe_list, shopping_list):
    click.echo("Shopping List for:")
    display_recipe_list(recipe_list)
    click.echo("")
    for ingredient in shopping_list:
        click.echo(ingredient[0])

if __name__ == "__main__":
    cli()