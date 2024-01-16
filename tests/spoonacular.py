import requests
from icecream import ic
from os import getenv
import dotenv
dotenv.load_dotenv('settings.env')
api = getenv('spoonacular')

ingredients = input("Enter ingredients : ")
url = "https://api.spoonacular.com/recipes/"

headers = {
    "apiKey":api,    
}


def search_by_ingredients(ingredients):
    """
	Searches for recipes by ingredients.

	Parameters:
	- ingredients: a list of strings representing the ingredients to search for.

	Returns:
	- meals: a dictionary with meal names as keys and a list of meal information as values. The meal information includes the meal image,meal id and a list of missing ingredients.
	"""

    headers['ingredients'] = ingredients
    headers['number'] = 5
    headers['ignorePanrty'] = 'false'
    ic("Sending Api request...")
    response = requests.get(f"{url}findByIngredients",params=headers)
    ic(f"Received response: {response}")
    data = response.json()
    meals = {} 
    for recipe in data:
        ic(recipe['title'])
        ic(recipe['id'])
        missed_ingredients = []
        for ingredient in recipe["missedIngredients"]:
          
            if ingredient['aisle'] == 'Spices and Seasonings': #pepper,salt..etc
                continue
            missed_ingredients.append(ingredient["name"])
        if len(missed_ingredients) <= 4:
            meals[recipe['title']] = [recipe['image'],recipe['id'],missed_ingredients]

        print()
        print()
        print()
    return meals




    



