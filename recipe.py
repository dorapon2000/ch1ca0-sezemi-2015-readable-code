import json

recipe_file = open('recipe-data.json', 'r')
recipe_json = json.load(recipe_file)

print(json.dumps(recipe_json, indent = 4))