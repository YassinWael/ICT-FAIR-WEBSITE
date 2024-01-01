import openai

client = openai.OpenAI(api_key='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')

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
    
    response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are an Experienced chef. Create 3 meals with provided ingredients ONLY. Specify cooking time for each, no cooking instructions."},
    {"role": "user", "content": f"{ingredients}, from {country}"}
  ]
)
    
    print(response.choices[0].message.content)


chatgpt("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",user_ingredients,country)