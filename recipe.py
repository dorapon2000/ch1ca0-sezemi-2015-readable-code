import json

recipe_file = open('recipe-data.json', 'r')
recipe_json = json.load(recipe_file)

recipe_list = recipe_json.keys()
for recipe_no, recipe in enumerate(recipe_list):
    print(str(recipe_no) + ": " +recipe)

