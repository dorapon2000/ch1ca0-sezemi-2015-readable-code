import json

recipe_file = open('recipe-data.json', 'r')
recipe_json = json.load(recipe_file)

recipe_list = recipe_json.keys()
for recipe in recipe_list:
    print(recipe)

