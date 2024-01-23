# main.py
from flask import Flask,request,render_template,make_response
from dotenv import load_dotenv
from os import getenv
from functions import search_by_ingredients,chatgpt_info,get_quote
from icecream import ic
from json import dumps,loads
load_dotenv('settings.env')
spoonacular_api = getenv('spoonacular')
chatgpt_api = getenv('OPENAI_API_KEY')
app_key = getenv('app_key')

url = "https://api.spoonacular.com/recipes/"

headers = {
    "apiKey":spoonacular_api,    
}







app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
  

    quote = get_quote()
    quote_list = request.cookies.get('quote_list')

    ic(quote_list)
    
    if not quote_list: 
        quote_list = ["With great Power, Comes great Responsibility"]
    else:
        
        quote_list = loads(quote_list) #Convert json string to list.
        while len(quote_list)>=3:
            quote_list.pop(0)
        quote_list.append(quote)
    past_quotes = quote_list
   
    for past in past_quotes:
        ic(past)
    json_list = dumps(quote_list) #Convert list to json string to send to page.
   
    
    
    response = make_response(render_template('home.html', quote=quote,past_quotes = past_quotes))
    response.set_cookie('quote_list', json_list) 
    ic(json_list)

    return response  # Return the response here, not render_template again


@app.route("/form",methods=['POST','GET'])
def search():
    if request.method == "POST":
        ingredients = request.form['ingredients']
        global recipes
        recipes = search_by_ingredients(ingredients)  #Dictionary with meals, and their info.
    return render_template('form.html')

@app.route("/recipes")
def recipes():
    global recipes
    recipes = search_by_ingredients(["Chicken","Egg","Meat"])
    for name,info in recipes.items():
        ic(name,info)
    return render_template('recipes.html',meals=recipes)

@app.route('/learn_more', methods=["GET","POST"])
def learn_more():
    
    meal_name = request.args.get('meal')
    ic(meal_name)

    
    content = chatgpt_info(meal_name,recipes[meal_name])
    return render_template('learn_more.html',content=content,name = meal_name,image = recipes[meal_name][0])



if __name__ == '__main__' :
    app.run(debug=True,port=8080,host="0.0.0.0")

# testing sync again.9