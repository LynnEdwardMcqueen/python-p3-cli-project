import click

def display_recipe_full(recipe_info):
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
            ingredient_string = " "*11 + ingredient[0] + " " + ingredient[2]
        else:
            ingredient_string = ("%11s" % (ingredient[0] + " " + ingredient[1] + " ")) + ingredient[2]
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

# Because of the complication of adding the ingredients via the command line, the user can interactively add the ingredients.
# The ingredients parameter has 0 length if it is not entered on the command line.  If this is true, this routine will
# prompt for new ingredients.
def get_new_recipe_ingredients(ingredients):
    if len(ingredients) == 0:
        i = 1
        ingredients =[]
        new_ingredient_amount = None
        while new_ingredient_amount != 'q':
            new_ingredient_amount = click.prompt(f'Enter ingredient {i} amount or q to quit > ')
            if new_ingredient_amount == "q":
                break
            new_ingredient_unit = click.prompt(f'Enter measurement unit (or None if no unit) of ingredient {i} > ')
            if new_ingredient_unit == "None":
                new_ingredient_unit = None
            new_ingredient_name = click.prompt(f'Enter the name of ingredient {i}')
            click.echo("")
            ingredients.append((new_ingredient_amount, new_ingredient_unit, new_ingredient_name))
            i += 1
    return ingredients

def get_new_recipe_instructions(instructions):
    if len(instructions) == 0:
        i = 1
        instructions = []
        new_instruction = None
        while new_instruction != "q":
            new_instruction = click.prompt(f"Enter instruction {i} or q to quit > ")
            if new_instruction == "q":
                break
            instructions.append(new_instruction)
            i += 1
    return instructions