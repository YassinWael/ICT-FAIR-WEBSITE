# main.py
from flask import Flask,request,render_template,make_response,send_file
from dotenv import load_dotenv
from os import environ
from functions import search_by_ingredients,chatgpt_info,get_quote
from icecream import ic
from json import dumps,loads
load_dotenv('settings.env')
spoonacular_api = environ.get('spoonacular')
chatgpt_api = environ.get('OPENAI_API_KEY')
app_key = environ.get('app_key')
ic(spoonacular_api,chatgpt_api,app_key)
url = "https://api.spoonacular.com/recipes/"

headers = {
    "apiKey":spoonacular_api,    
}







app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
  

    quote = get_quote()
    global past_meals
    past_meals = request.cookies.get('past_meals')

    ic(past_meals)
    
    if not past_meals: 
        past_meals = ["Eggs with cheese"]
    else:
        past_meals = loads(past_meals) #Convert json string to list.
        while len(past_meals)>=3:
            past_meals.pop(0)
   
   
    for past in past_meals:
        ic(past)
    json_list = dumps(past_meals) #Convert list to json string to send to page.
   
    
    
    response = make_response(render_template('home.html', quote=quote,past_meals=past_meals))
    response.set_cookie('past_meals', json_list) 
    ic(json_list)

    return response  # Return the response here, not render_template again


@app.route("/form",methods=['POST','GET'])
def form():
    if request.method == "POST":
        ingredients = []
        try:
            for i in range(1,6):
                print(i)
                ingredients.append(request.form[f'in{i}'])
        except Exception as e:
            pass
        
        ic(ingredients)
        global recipes
       
        recipes = search_by_ingredients(ingredients)  #Dictionary with meals, and their info.
        ic(recipes)
    
        return render_template('recipes.html',meals=recipes,past_meals=past_meals)

    ic(f"form,: {past_meals} ")
    return render_template('form.html',past_meals=past_meals)

@app.route("/recipes")
def recipes():
    global recipes
    for name,info in recipes.items():
        ic(name,info)
    return render_template('recipes.html',meals=recipes,past_meals=past_meals)

ic("Here")
@app.route('/learn_more', methods=["GET","POST"])
def learn_more():
 
    meal_name = request.args.get('meal')
    past_meals = request.cookies.get('past_meals')    
    if not past_meals: 
        past_meals = ["Eggs with cheese"]
    else:
        past_meals = loads(past_meals) #Convert json string to list.
        while len(past_meals)>=3:
            past_meals.pop(0)
        past_meals.append(meal_name)
   
   
    for past in past_meals:
        ic(past)
    json_list = dumps(past_meals) #Convert list to json string to send to page.
   
    
    
    
    response = make_response(render_template('learn_more.html',content=chatgpt_info(meal_name,recipes[meal_name]),name = meal_name,image = recipes[meal_name][0],past_meals = past_meals))
    response.set_cookie('past_meals', json_list) 
    ic(json_list)

    return response

@app.route('/OneSignalSDKWorker.js')
def push_notifications():
    return send_file('OneSignalSDKWorker.js')
    



if __name__ == '__main__' :
    app.run(debug=True,port=8080,host="0.0.0.0")

# testing sync again.9