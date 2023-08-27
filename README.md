# Recipe cli Project

## Project Goals

- Create a recipe database with a command line interface (Cli)
- Provide basic functionality:  Add/Delete Recipe, Display Recipe, Display Recipe List, Change Recipe Title.
- Provide a shopping list given a set of recipes.  With multiple growing teens in the house, I can never take for granted that the required ingredients are in the cupboards and pantry.
- Show the food pyramid information given a set of recipes.  It's not the best approach to nutrition.  I just want to make sure that the choices I'm making are somewhat balanced and include a variety of nutritional ingredients.
- Retrieve recipes given a particular ingredient.  In this day of Costco Warehouse shopping, I need to know what I can do with my 5 pound purchase of Ricotta cheese.




***

## Environment Setup

This project includes Pipfile to support configuring your environment to run the program.  This program requires alembic, sqlalchemy, python, and click packages.  It provides ipdb support in case you decide to dive in an debug.  To correctly configure your environment, from the project root directory run
- pipenv install python
- pipenv install alembic
- pipenv install sqlalchemy
- pipenv install click

Additionally, you will need to install sqlite3.  For Windows machines (which is what I used), you need to run the following from the WSL terminal.
- Update your Ubuntu packages by running: sudo apt update
- Once the packages have updated, install SQLite3 with: sudo apt install sqlite3

Now run pipenv shell to run with all the packages correctly configured.


## Running the program

To run this program, cd to the lib directory of the project.  The project uses the click python package.  All commands are contained in the cli.py file.  To see the available commands, type python cli.py --help.  You will see the following as shown in the example below.
```
lynn@DESKTOP-75E266D:~/Development/code/phase3/python-p3-cli-project/lib$ python cli.py --help
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add-recipe            Adds a new recipe to the list.
  change-recipe-title   Changes the name/title of a recipe.
  create-shopping-list  Creates a shopping list from a list of recipe ids
  delete-recipe         Deletes a recipe from the database
  display-recipe        Takes a recipe id and displays the recipe details
  list-recipes          Displays the recipe ids and titles
  matching-ingredient   Displays a list of recipes containing an ingredient
  show-pyramid-info     Returns the nutrition pyramid info for a recipe...
```
Help for individual commands is available also.  For example, help for the matching-ingredient command is:
```
lynn@DESKTOP-75E266D:~/Development/code/phase3/python-p3-cli-project/lib$ python cli.py matching-ingredient --help
Usage: cli.py matching-ingredient [OPTIONS] INGREDIENT

  Displays a list of recipes containing an ingredient

  INGREDIENT is the search ingredient.

Options:
  --help  Show this message and exit.
```


## File Descriptions
The program consists of 4 main python files:
- cli.py
- cmdprocessor.py
- helpers.py
- models.py

### cli.py
The cli.py file uses the python click package for handling the user input and printing to the screen.  The following functions are in the file.
- add_recipe
- change_recipe_title 
- display_recipe
- list_recipes
- matching_ingredient
- show_pyramid_info


 
#### add_recipe
The add_recipe gets the title, food pyramid information, ingredients, and instructions for a new recipe from the user and commits them to the data base.

#### change_recipe_title
This routine takes a recipe index and title string and alters the title of the recipe in the data base.

#### display_recipe
This routine takes a recipe index and returns the title, ingredient list, and instruction list for the recipe.

#### list_recipes 
This routine returns the recipe title and index for every recipe in the database.

#### matching_ingredient
This routine takes an ingredient from the user, searches the database for it and returns a list of recipes that include it in their ingredient list.

#### show_pyramid_info
show_pyramid_info takes a list of recipe indices and returns the food pyramid information for the collection of recipes.

### cmdprocessor.py
This file contains all the functionality needed to interface with the sqlalchemy package.  It takes the requests from the cli and performs the database operations.

#### helper.py
This file contains the functions for handling the I/O associated with the commands in cli.py.

#### model.py
This file contains the sqlalchemy database model.  There are 3 tables:
- Recipe
- Ingredient
- Instruction

The Recipe and Ingredient tables share a 1 to many relationship (i.e., 1 recipe entry is related to multiple ingredient entries).  The Recipe and Instruction tables also share a 1 to many relationship (i.e, 1 recipe entry is related to multiple instruction entries).
