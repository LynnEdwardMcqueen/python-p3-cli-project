from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Recipe, Ingredient, Instruction


    

recipe_preload = (
    (
        ("Creamy Chicken Pesto Pasta", 1, 1, 1, 0, 0),
        (
            "Season and grill the chicken or you can use rotisserie chicken too. Cube the cooked chicken and toss in 1/2 cup pesto. Set aside. Cook the pasta to al dente",
	        "Preheat oven to 350°F/175°C",
	        "Meanwhile, mix the pasta sauce and 1/2 cup pesto together in a medium bowl. Set aside.",
            "In a large bowl, mix together ricotta, cottage cheese, 1 cup mozzarella, spinach, parmesan, and eggs. Then add the cooked pasta to the cheese mixture and gently stir to combine.",
            "In a 9x13 (or two 8x8 pans), layer sauce, pasta mixture, chicken, sauce, pasta mixture, chicken, sauce. Bake in a preheated oven for 40 minutes uncovered, top with remaining mozzarella and bake for 5 minutes more."
        ),
        ( 
            ("1", "lb.", "chicken"),
            ("1", "C", "pesto divided"),
            ("14.5", "oz.", "penne pasta"),
            ("48", "oz.", "pasta sauce"),
            ("8", "oz.", "part skim ricotta cheese"),
            ("8", "oz.", "cottage cheese"),
            ("1", "C", "frozen chopped spinach thawed and drained"),
            ("1/4", "C", "parmesan cheese"),
            ("2",None ,"large eggs"),
            ("2", "C", "mozzarella cheese divided")
        ),
    ),
    (
	    ("Garlic Pork Stir-Fry", 1,0,0,1,0),
	    (
            "Rinse and trim pork loin as desired. Cut pork into about 1-inch cubes.",
	        "In a medium bowl, whisk together soy sauce, vinegar, and sugar. Whisk in the garlic and crushed red pepper.",
	        "Place cubed pork into a 1-quart freezer bag, add 1 cup cornstarch to the bag; seal bag and shake to coat the meat.",
	        "In a large skillet, heat the oil over medium-high heat. Add pork and stir-fry until cooked, about 10 minutes.",
            "Add vegetables and sauce. Stir-fry until vegetables are tender and crisp. Serve with rice, if desired."
	    ),
	    (
            ("3", "lb.", "pork loin or pork roast"),
	        ("1", "C", "cornstarch"),
	        ("4", "t", "oil"),
	        ("3/4", "C", "soy sauce"),
	        ("1/4", "C", "white wine vinegar"),
        	("1", "t", "sugar"),
	        ("4", "t", "minced garlic"),
	        ("1/2", "t", "crushed red pepper flakes"),
	        ("2", None, "onions cut into 2-inch pieces or diced"),
	        ("1", None, "green bell pepper cut into 2-inch pieces or diced"),
	        ("1", None, "red bell pepper cut into 2-inch pieces or diced")
        )
    ),
    (
	    ("Instant Pot Chicken Noodle Soup", 1, 1, 0, 1, 0),
	    (
            "On Instant Pot, press saute button. After 1 minute, add olive oil to IP insert. Wait 1 minute, then add onion and garlic. Saute, stirring often, for 1 minute. Add carrots and celery and saute for 2 minutes. Add diced chicken and Italian seasoning and cook, stirring often, until almost done.",
	        "Add remaining ingredients, making sure the noodles are just covered with liquid.",
	        "Cover the IP with lid and set the pressure valve to sealing position. Newer models do it on their own.",
	        "Press manual and set the timer to 6 minutes. Make sure your Instant Pot is set to high pressure. The pressure cooker will beep and start coming to pressure, which can take about 12 minutes.  When the cooking time is up, press the cancel/off button. Let the pressure release naturally for 5 minutes (to let the foam from cooking noodles to fall)", 
	        "then quick release any remaining pressure by switching the valve to venting position.",
	        "Carefully open the lid, away from your face. Stir the soup. Let cool and serve. Adjust seasoning as needed"
	    ),
	    (
            ("1", "t", "olive oil"),
        	("3", None, "garlic cloves minced"),
	        ("1", "C", "chopped yellow onion"),
	        ("2", None, "boneless skinless chicken breast cut into 1 inch cubes"),
	        ("2", "t", "Italian seasoning or fresh poultry herb blend"),
	        ("2", "C", "diced carrots"),
            ("4", None, "celery ribs diced"),
	        ("3", "C", "wide egg noodles dry, not yet cooked"),
	        ("4", "C", "chicken stock or broth"),
	        ("3", "C", "water"),
	        ("1", "t", "dried oregano"),
	    )
    ),
    (
        ("Instant Pot Creamy Italian Pasta", 0, 1, 1,0, 0),
        (
            "Pour the broth into the inner pot. Stir in the wine, garlic, oregano, pepper, black pepper, and crushed red pepper flakes, if using.",
            "Pour the pasta into the inner pot. gently pushing down to submerge in the broth. Then top the dry pasta with the diced tomatoes and spaghetti sauce, spreading to evenly cover the pasta. Dollop with ricotta cheese, if using.",
            "Cook on high pressure for 4 minutes for rotini and corkscrew noodles and 5 minutes for ziti or rigatoni noodles. Alternatively, set the cooking time for HALF the lowest suggested cook time on the box of pasta.",
            "Once the cooking time has elapsed, allow the pressure to release for exactly 5 minutes, then do a quick release of the remaining pressure. To do a quick release, stand away from the vent knob, and use a long utensil to knock the venting knob from the sealed to the venting position.",
            "Give the noodles a gentle stir into the sauce to combine. Top with the parmesan and mozzarella, and place the lid back on the inner pot for 2-5 minutes, to melt the cheese.",
            "Serve immediately."
        ),
        (
            ("2-1/2", "C", "chicken or vegetable broth"),
            ("1/2", "C", "dry red wine or addtional stock"),
            ("2", "t", "minced garlic"),
            ("1/2", "t", "dried oregano"),
            ("1/4", "t", "kosher salt"),
            ("1/8", "t", "black pepper"),
            ("1/8", "t", "crushed red pepper flakes"),
            ("16",  "oz.", "dried pasta ziti, rotini, corkscrew, rigatoni, etc"),
            ("15",  "oz.", "diced tomatoes"),
            ("24", "oz.", "spaghetti sauce"),
            ("8", "oz.", "ricotta cheese"),
            ("1/4", "C", "parmesan cheese"),
            ("1", "C", "mozzarella cheese shredded"),
        )
   ),
   (
	    ("Black Bean Taco Soup",1, 1,0,1,0),
	    (
            "Brown meat and onion, drain.",
	        "Stir in taco seasoning, corn, black beans, tomatoes, tomato sauce, and green chilis. Simmer on low heat for 20 to 30 minutes."
	        "Serve with tortilla chips and your favorite toppings."
	    ),
	    (
            ("1", "lb.", "ground turkey"),
	        ("1",None, "onion chopped"),
	        ("1", "oz.", "taco seasoning"),
	        ("15.25", "oz.", "canned corn do not drain"),
	        ("15", "oz.", "black beans rinsed and drained"),
	        ("14.5", "oz.", "stewed tomatoes do not drain"),
	        ("14.5", "oz.", "diced tomatoes do not drain"),
	        ("8", "oz.", "tomato sauce"),
	        ("4", "oz.", "diced green chilis"),
	        ("11", "oz.", "tortilla chips"),
	        ("1/2", "C", "shredded cheddar cheese optional topping")
	    )
    ),
    (
    	("Chicken, Broccoli, Bacon & Potato Bake", 1, 1, 1, 1, 1),
	    (   
            "Grease 2 8×8 foil baking pans.",
	        "Divide ingredients in half – you are making 2 pans, so half of the ingredients goes in each pan.",
	        "In both pans, layer ingredients in this order: potatoes, chicken, broccoli, bacon, onion and cheese.",
	        "Season with salt, pepper and garlic powder.",
	        "Repeat the layers and seasoning.",
	        "Pour heavy cream over ingredients and sprinkle butter pieces over the dish.",
	        "Cover with foil"
	    ),
        (		
	        ("4-1/2", "C", "red potatoes (diced)"),
	        ("2-1/2", "C", "boneless skinless chicken breast (diced )"),
	        ("2", "C", "broccoli florets"),
	        ("1/2", "C", "bacon (cooked crumbled)"),
	        ("1/4", "C", "onion (sliced )"),
	        ("2", "C", "cheddar cheese (grated)"),
	        ("1/2", "t", "salt"),
	        ("1/4", "t", "cracked pepper"),
	        ("1/2", "t", "garlic powder"),
	        ("1", "C", "heavy cream ((can sub half & half))"),
	        ("2", "T", "butter (chopped)"),
	        ("1", "C", "cheddar cheese (grated)")
        )
    ),
    (
	    ("Cobb Salad", 1, 0, 1, 1, 0),
	    (
            "Place eggs in a saucepan and cover completely with cold water; bring to a boil, then cover and remove from heat. Let eggs sit for 10 to 12 minutes, then cool, peel and chop.",
	        "While the eggs are cooking, place bacon in a large, deep skillet. Cook over medium-high heat until evenly brown, 7 to 10 minutes. Drain, crumble, and set aside.",
	        "Divide shredded lettuce among individual plates. Top with rows of bacon, eggs, chicken, tomatoes, blue cheese, green onions, and avocado.",
	        "Drizzle with dressing."
	    ),
	    (
            ("6", None, "slices bacon"),
	        ("3", None, "eggs"),
	        ("1", None, "head iceberg lettuce, shredded"),
	        ("3", "C", "chopped, cooked chicken meat"),
	        ("2", None, "tomatoes, seeded and chopped"),
	        ("3/4", "C", "blue cheese, crumbled"),
	        ("3", None, "green onions, chopped"),
	        ("1", None, "avocado - peeled, pitted and diced"),
	        ("1", None, "bottle Ranch-style salad dressing")
	    )
    ),
    (
	    ("Instant Pot Ground Beef Stroganoff", 0, 1, 1, 1, 1),
	    (
            "Spray Instant Pot interior with cooking spray. Set to saute.",
	        "Brown ground beef, onion, and garlic.",
	        "After beef is browned stir in flour.",
	        "Add broth, soup, and salt and pepper. Mix.",
	        "Add noodles.",
	        "Place lid on Instant Pot.",
	        "Set to high pressure for 8 minutes.",
	        "After it is done, let the pressure naturally release for about five minutes, and then change to quick release until all the pressure is gone.",
	        "Stir in sour cream until combined."
	    ),
	    (   
            ("1/2", "C", "minced onion"),
	        ("1", None, "clove garlic minced"),
	        ("1", "lb.", "ground beef"),
	        ("1", "t", "salt"),
	        ("1/4", "t", "pepper"),
	        ("10.5", "oz.", "can cream of mushroom soup"),
	        ("1", "T", "Flour"),
	        ("3", "C", "beef broth"),
	        ("3", "C", "egg noodles uncooked"),
	        ("1", "C", "sour cream")
	    )
    )
) 

if __name__ == '__main__':
    engine = create_engine('sqlite:///recipes.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    for current_recipe in recipe_preload:
        recipe_data = current_recipe[0]

        recipe = Recipe(recipe_title = recipe_data[0],
            vegetables_and_fruit = recipe_data[1],
            breads_and_cereals = recipe_data[2],
            dairy = recipe_data[3],
            meat = recipe_data[4],
            fats_and_sugar = recipe_data[5]
            )
        
        session.add(recipe)
        session.commit()
    

        for instruction in current_recipe[1]:
            instruction_row = Instruction(instruction = instruction,
                recipe_id = recipe.id)

            session.add(instruction_row)
            session.commit()

        for ingredient in current_recipe[2]:
            ingredient_row = Ingredient(measurement_amount = ingredient[0],
                measurement_unit = ingredient[1],
                ingredient = ingredient[2],
                recipe_id = recipe.id)            
            session.add(ingredient_row)
            session.commit()



