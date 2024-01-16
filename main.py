# main.py
from flask import Flask,request,render_template
from dotenv import load_dotenv
from os import getenv
from functions import search_by_ingredients,chatgpt_info
load_dotenv('settings.env')
spoonacular_api = getenv('spoonacular')
chatgpt_api = getenv('chatgpt')
app_key = getenv('app_key')

url = "https://api.spoonacular.com/recipes/"

headers = {
    "apiKey":spoonacular_api,    
}







app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/search",methods=['POST','GET'])
def search():
    if request.method == "POST":
        ingredients = request.form['ingredients']
        global recipes
        recipes = search_by_ingredients(ingredients)  #Dictionary with meals, and their info.
    return render_template('search.html')

if __name__ == '__main__' :
    app.run(debug=True)

# testing sync again.9