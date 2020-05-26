from book import Book
from recipe import Recipe
from datetime import datetime
tourte = Recipe("tryu", 5, 8, ["qssf", "xdf"], "starter")
# # name
# tourte = Recipe("", 5, 8, ["qssf", "xdf"], "starter")
#
# # cooking_lvl
# tourte = Recipe("tryu", 6, 8, ["qssf", "xdf"], "starter")
# tourte = Recipe("tryu", 0, 8, ["qssf", "xdf"], "starter")
#
# # cooking_time
# tourte = Recipe("tryu", 5, -1, ["qssf", "xdf"], "starter")
# tourte = Recipe("tryu", 5, "df", ["qssf", "xdf"], "starter")
#
# # ingredients
# tourte = Recipe("tryu", 5, 8, "sdf", "starter")
# tourte = Recipe("tryu", 5, 8, [1], "starter")
# tourte = Recipe("tryu", 5, 8, [], "starter")
# tourte = Recipe("tryu", 5, 8, [""], "starter")
# tourte = Recipe("tryu", 5, 8, ("qssf", "xdf"), "starter")
#
# # recipe_type
# tourte = Recipe("tryu", 5, 8, ["qssf", "xdf"], "")
# tourte = Recipe("tryu", 5, 8, ["qssf", "xdf"], 1)
# tourte = Recipe("tryu", 5, 8, ["qssf", "xdf"], "starterp")
# tourte = Recipe("tryu", 5, 8, ["qssf", "xdf"], "starter", 1)

dict = {"starter": [],  "lunch": [], "dessert": []}
dict_false = {"starter": "sd",  "lunch": ""}
dict_false2 = {"starter": "sd",  "lunch": "", "dessert": "", "dsf": "sqd"}
dict_false3 = {"starterd": "sd",  "lunch": "", "dessert": ""}
# book = Book("sd", datetime(2020, 1, 3), datetime(2020, 2, 3), dict_false)
# book = Book("sd", datetime(2020, 1, 3), datetime(2020, 2, 3), dict_false2)
# book = Book("sd", datetime(2020, 1, 3), datetime(2020, 2, 3), dict_false3)
book = Book("sd", datetime(2020, 1, 3), datetime(2020, 2, 3), dict)
tourte = Recipe("tourte", 5, 8, ["qssf", "xdf"], "starter")
tourte2 = Recipe("tourte2", 5, 8, ["qssf", "xdf"], "starter")

tourte_bad = Recipe("tourte3", 5, 8, ["qssf", "xdf"], "starter")
book.add_recipe(tourte)
book.add_recipe(tourte2)
# book.add_recipe(tourte_bad)

# get_recipes_by_types
book.get_recipes_by_types("starter")
book.get_recipes_by_types("dessert")

# get_recipe_by_name
re = book.get_recipe_by_name("tourte")
print(re)
