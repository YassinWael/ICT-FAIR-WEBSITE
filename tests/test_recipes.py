import openai



user_ingredients = input("Tell us what you have, We only assume water and salt :  ") + " Water and salt"
country = input("Enter your country (Optional):  ")

def chatgpt(api,ingredients,country=""):
    """
    Generates a chat-based prompt for the OpenAI GPT-3.5-turbo model to retrieve 5 food suggestions based on a given list of ingredients and an optional country.

    Args:
        api (str): The API key for accessing the OpenAI API.
        ingredients (str): The list of ingredients to base the food suggestions on.
        country (str, optional): The country to consider when generating the food suggestions. Defaults to "".

    Returns:
        None
    """
    

    prompt =  f"hello, based ONLY (NO MATTER HOW MUCH THE INGREDIENTS IS SMALL, ONLY USE THOSE) on the following ingredients: '{ingredients}', Name 5 {country} foods that I can make. Talk in an intuitive way and catchy while using simple words, also mention how much approximately the time needed to cook this" if country else f"hello, based ONLY on {user_ingredients}, Name 5 foods that I can make. Talk in an intuitive way and catchy while using simple words, also mention how much approximately the time needed to cook this" 
    print(prompt)
    from pyperclip import copy
    copy(prompt)
    openai.api_key = api
    response = openai.Completion.create(
        model="Gpt-3.5-turbo",  
        prompt= prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
    )


chatgpt("12421432",user_ingredients,country)