import json
import sys

recipe_file = open('recipe-data.json', 'r')
recipe_json = json.load(recipe_file)

recipe_list = recipe_json.keys()
for recipe_no, recipe in enumerate(recipe_list):
    if sys.argv.length() == 1:        
        print(str(recipe_no) + ": " +recipe)
    else:
        show_recipe_no = sys.argv[1] #sys.argvの表示が2つになってる
