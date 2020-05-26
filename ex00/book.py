from datetime import datetime
from recipe import Recipe


class Book():
    """docstring for Book."""

    def __init__(self, name, last_update, creation_date, recipes_list):
        if (isinstance(name, str)):
            self.name = name
        else:
            self.my_exit(f"Bad type for name: ({name})")
        if (isinstance(last_update, datetime)):
            self.last_update = last_update
        else:
            self.my_exit(f"Bad type for last_update: ({last_update})")
        if (isinstance(creation_date, datetime)):
            self.creation_date = creation_date
        else:
            self.my_exit(f"Bad type for creation_date: ({creation_date})")
        if (isinstance(recipes_list, dict) and len(recipes_list.keys()) == 3):
            if all(k in {"starter", "lunch", "dessert"} for k in recipes_list):
                self.recipes_list = recipes_list
            else:
                self.my_exit(f"Bad key in recipes_list: ({recipes_list})")
        else:
            self.my_exit(
                f"Bad type or bad length for recipes_list: ({recipes_list})")

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for x in self.recipes_list:
            for y in self.recipes_list[x]:
                if (y.name == name):
                    print(y)
                    print()
                    return y

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if (recipe_type in ["starter", "lunch", "dessert"]):
            for x in self.recipes_list[recipe_type]:
                print(x)
                print()
        else:
            print(f"Bad type ({recipe_type})")

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        # self.recipes_list.update({recipe.recipe_type: recipe})
        if (isinstance(recipe, Recipe)):
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()
        else:
            print("Bad recipe type")

    def my_exit(self, str):
        print(str)
        exit()
