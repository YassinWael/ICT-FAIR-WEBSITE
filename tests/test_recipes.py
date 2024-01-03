import openai
from dotenv import load_dotenv
from os import getenv
from re import findall
from icecream import ic
# Loading API
load_dotenv('settings.env')
api = getenv('api')
client = openai.OpenAI(api_key=api)

pattern = "\*(.*?)\*"
pattern2 = "\*\*(.*?)\*\*" #chatgpt some times put two astericks

user_ingredients = input("Tell us what you have, We only assume water and salt :  ") + " Water and salt and pepper"
country = input("Enter your country (Optional):  ")

def chatgpt(ingredients,country="mix of contries"):
    """
    Generates a chat-based prompt for the OpenAI GPT-3.5-turbo model to retrieve 5 food suggestions based on a given list of ingredients and an optional country.

    Args:
        api (str): The API key for accessing the OpenAI API.
        ingredients (str): The list of ingredients to base the food suggestions on.
        country (str, optional): The country to consider when generating the food suggestions. Defaults to "".

    Returns:
        None
    """
    
    response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    
    {"role": "system", "content": "As an Experienced chef, craft 3 meals from the specified country using only provided ingredients. Place meal names in asterisks, e.g., *French Toast*. Verify each step's ingredients; if missing, pick an alternative. Be creative, prioritize taste, If there is a popular meal with the ingredients given make sure to mention it. Note differences between user's and needed ingredients with #, e.g., #cheese#."},
    {"role": "assistant", "content": "Here is a small example: User's ingredients (the only ingredients i can use) are bread,yogurt some tomato and sugar and he didn't specify a country so anywhere should be fine, 1. *Simple Tomato Sandwitch* Instructions : 'Toast the bread and spread some yogurt on it. Add sliced tomatoes and sprinkle some sugar on top.' 2.*Tomato yogurt salad* instructions: 'Cut the tomatoes into small pieces and mix them with yogurt. Add some sugar to taste.' 3.*Tomato yogurt dip* instructions 'Mix yogurt, chopped tomatoes, and sugar in a bowl. Use this as a dip for bread.'"},
    {"role": "user", "content": f"{ingredients}, from {country}"}
  ]
)
    
    chatgpt_answer = (response.choices[0].message.content)
    tokens_total = response.usage.total_tokens
    ic(tokens_total)
    print(chatgpt_answer)
    meal_names = findall(pattern,chatgpt_answer)
    if not meal_names:
        meal_names = findall(pattern2,chatgpt_answer)
    print(meal_names)
    print(len(meal_names))


chatgpt(user_ingredients,country)