class Recipe():
    """docstring for Recipe."""

    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 r_t, description=""):

        if (isinstance(name, str) and len(name) > 0):
            self.name = name
        else:
            self.my_exit(f"Bad length or bad type for name: ({name})")
        if (isinstance(cooking_lvl, int) and 1 <= cooking_lvl <= 5):
            self.cooking_lvl = cooking_lvl
        else:
            self.my_exit(
                f"Bad value or bad type for cooking_lvl: ({cooking_lvl})")
        if (isinstance(cooking_time, int) and 0 <= cooking_time):
            self.cooking_time = cooking_time
        else:
            self.my_exit(
                f"Bad value or bad type for cooking_time: ({cooking_time})")
        if (isinstance(ingredients, list) and ingredients):
            for x in ingredients:
                if not isinstance(x, str) or not x:
                    self.my_exit(
                        f"Bad type for ingredient in ingredients: ({x})")
            self.ingredients = ingredients
        else:
            self.my_exit(
                f"Bad value or bad type for ingredients: ({ingredients})")
        if (isinstance(r_t, str)
                and (r_t == "starter" or r_t == "lunch" or r_t == "dessert")):
            self.recipe_type = r_t
        else:
            self.my_exit(f"Bad value or bad type for recipe_type: ({r_t})")
        if (isinstance(description, str)):
            self.description = description
        else:
            self.my_exit(f"Bad type for description: ({description})")

    def my_exit(self, str):
        print(str)
        exit()

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += (f"Recipe for {self.name}:\n")
        txt += (f"Cooking level: {self.cooking_lvl}:\n")
        txt += (f"Ingredients list: {self.ingredients}\n")
        txt += (f"To be eaten for {self.recipe_type}.\n")
        txt += (f"Takes {self.cooking_time} minutes of cooking.\n")
        txt += (f"Description: {self.description}")
        return txt
