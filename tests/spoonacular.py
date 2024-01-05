import requests
import json
from icecream import ic
from os import getenv
import dotenv
dotenv.load_dotenv('settings.env')
api = getenv('spoonacular')

ingredients = input("Enter ingredients : ")
url = "https://api.spoonacular.com/recipes/"

headers = {
    "apiKey":api,
    "ingredients":ingredients,
    "number":8,
    "sort":"min-missing-ingredients",
    "ignorePantry":"false"
}


def search_by_ingredients(ingredients):

    headers['ingredients'] = ingredients

    response = requests.get(f"{url}findByIngredients",params=headers)
    ic(response)
    data = response.json()
    ic(data)
    meals = {} #dictionary with meal name,image and missing ingrdeints
    for recipe in data:
        ic(recipe['title'])

        missed_ingredients = []
        for ingredient in recipe["missedIngredients"]:
            if ingredient['aisle'] == 'Meat': #removes meals in which Meat is needed and is missing
                missed_ingredients.append("Break")

            if ingredient['aisle'] == 'Spices and Seasonings': #pepper,salt..etc
                continue
            missed_ingredients.append(ingredient["name"])
        if len(missed_ingredients) <= 3 and "Break" not in missed_ingredients:
            meals[recipe['title']] = [recipe['image'],missed_ingredients]
        ic(f"for {recipe['title']} : {' and '.join(missed_ingredients)} are missing ingredients")
        print()
    return meals

meals = search_by_ingredients(ingredients)
print(meals)
    



