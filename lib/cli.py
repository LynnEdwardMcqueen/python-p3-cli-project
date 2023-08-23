from helpers import Helper
import click

@click.group()
def cli():
    pass    

@click.argument("recipe_ids", nargs = -1)
@cli.command()
def displayrecipes(recipe_ids):
    click.echo(f"The recip_numbers = {recipe_ids}")
    # Click sends all arguments as tuple of strings.  They need to be converted to
    # integers
    int_recipe_ids = [int(str_id) for str_id in recipe_ids ]
    click.echo(f"The real recipe indices are {int_recipe_ids}")

@click.option("-a", "--alpha", is_flag = True, show_default = True, default = 0)
@cli.command()
def listrecipes(alpha):
    click.echo(f"Here in listrecipes, alpha = {alpha}")
    recipe_list = Helper.get_recipe_list(alpha)
    display_recipe_list(recipe_list)


def display_recipe_list(recipe_list):
    for recipe_item in recipe_list:
        display_string = "  ".join( (str(recipe_item[0]),recipe_item[1]) )
        click.echo(display_string)

if __name__ == "__main__":
    cli()