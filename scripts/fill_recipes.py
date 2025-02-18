from core.models import Recipe, CustomUser
import requests

def run():
    res = requests.get('https://dummyjson.com/recipes')
    recipes = res.json()

    if recipes:
        for data in recipes['recipes']:
            name = data.get('name')
            cuisine = data.get('cuisine')
            difficulty = data.get('difficulty')
            rating = data.get('rating')
            ingredients = data.get('ingredients')
            instructions = data.get('instructions')

            Recipe.objects.create(
                name=name,
                cuisine=cuisine,
                difficulty=difficulty,
                rating=rating,
                ingredients=ingredients,
                instructions=instructions,
                user=CustomUser.objects.first(),
            )
    
