from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '334a795cb7074feaba47f0d1645371c5' # You can get your own API key from https://spoonacular.com/food-api
API_URL = 'https://api.spoonacular.com/recipes/findByIngredients'
DETAILS_API_URL = 'https://api.spoonacular.com/recipes/{}/information'  # For detailed recipe info

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_recipe():
    ingredients = request.form.get('ingredients')
    
    if not ingredients:
        return render_template('index.html', error="Please provide ingredients.")
    
    # Prepare the parameters for the API request
    params = {
        'ingredients': ingredients,  # e.g., "chicken,tomato,onion"
        'number': 5,  # Number of recipes to return
        'apiKey': API_KEY
    }
    
    # Make the API request
    response = requests.get(API_URL, params=params)
    
    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        return render_template('index.html', error="Failed to fetch recipes from the API.")
    
    recipes = response.json()

    # Handle case when no recipes are returned
    if not recipes:
        return render_template('index.html', error="No recipes found for the given ingredients.")
    
    # Render the recipes page with the data
    return render_template('recipes.html', recipes=recipes)

@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    # Fetch detailed recipe information using the recipe id
    details_url = DETAILS_API_URL.format(recipe_id)
    params = {'apiKey': API_KEY}
    response = requests.get(details_url, params=params)
    
    if response.status_code != 200:
        return render_template('error.html', error="Failed to fetch recipe details.")
    
    recipe_details = response.json()

    # Render the detailed recipe view
    return render_template('recipe_details.html', recipe=recipe_details)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

