import requests
from dotenv import load_dotenv
from os import environ
from icecream import ic
import openai

# Loading keys
load_dotenv('settings.env')
spoonacular_api = environ.get('spoonacular')
chatgpt_api = environ.get('OPENAI_API_KEY')
app_key = environ.get('app_key')

url = "https://api.spoonacular.com/recipes/"

headers = {
    "apiKey":spoonacular_api,    
}
def search_by_ingredients(ingredients):
    """
    Searches for recipes based on a list of ingredients.

    Parameters:
        ingredients (list): A list of ingredients to search for.

    Returns:
        dict: A dictionary containing the meals found. Each key is a recipe title, and the value is a list containing the recipe image URL, recipe ID, a list of used ingredients, and a list of missed ingredients.
    """
   
    headers['ingredients'] = ingredients
    headers['number'] = 8
    headers['ignorePanrty'] = 'true'
    ic(f"Sending Api request...: {headers['apiKey']}")
    response = requests.get(f"{url}findByIngredients",params=headers)
    ic(f"Received response: {response}")
    data = response.json()
    ic(data)
    meals = {} 

    for recipe in data:
        ic(recipe)
        ic(recipe['title'])
        ic(recipe['id'])
        missed_ingredients = []
        for ingredient in recipe["missedIngredients"]:
          
            if ingredient['aisle'] == 'Spices and Seasonings': #pepper,salt..etc
                continue
            missed_ingredients.append(ingredient["name"])

        
        used_ingredients = []
        for ingredeint in recipe['usedIngredients']:
            used_ingredients.append(ingredeint["name"])
        if len(missed_ingredients) <= 4:
            meals[recipe['title']] = [recipe['image'],recipe['id'],used_ingredients,missed_ingredients]

        print()
        print()
        print()
    return meals
ic("-------------------------------------------")
ic("-------------------------------------------")
ic("-------------------------------------------")
ic("-------------------------------------------")
ic("-------------------------------------------")
ic("-------------------------------------------")
ic("-------------------------------------------")

# print(meals)
def chatgpt_info(meal,info):
    """
    Generate a chat response using the OpenAI GPT-3.5-turbo model.

    Parameters:
    - meal (str): The desired meal to cook.
    - info (list): A list containing 4 elements:
        - Element 0 (str): The API key for accessing the OpenAI API.
        - Element 1 (str): The prompt for the chat completion.
        - Element 2 (list): A list of ingredients to include in the meal.
        - Element 3 (list): A list of ingredients to exclude from the meal.

    Returns:
    - answer (str): The chat response generated by the GPT-3.5-turbo model.
    """

    client = openai.OpenAI(api_key=chatgpt_api)
    prompt = f"Cook {meal} only with {' and '.join(info[2])}, excluding {' and '.join(info[3])}. Be concise. Use simple words. Answer in a user-friendly way"

    print(prompt)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    answer = (response.choices[0].message.content)
    print(answer)
    return answer
# recipes = search_by_ingredients(["Chicken","Egg","Meat"])
# for meal_name in recipes:
#     chatgpt_info(meal_name,recipes[meal_name])

def get_quote():
    """
    Function to retrieve a quote from an external API with a maximum length of 50 characters.
    Returns the content of the quote.
    """
    headers['maxLength'] = 40
    params = requests.get('https://api.quotable.io/quotes/random',params=headers).json()
    return params[0]['content']

def get_quote():
    """
    Function to retrieve a quote from an external API with a maximum length of 50 characters.
    Returns the content of the quote.
    """
    headers['maxLength'] = 40
    params = requests.get('https://api.quotable.io/quotes/random',params=headers).json()
    return params[0]['content']

