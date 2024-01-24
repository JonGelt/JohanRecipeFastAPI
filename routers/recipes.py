from fastapi import APIRouter
from models.recipe_model import Recipe

router = APIRouter()

recipes = []

@router.get("/recipes/")
def get_recipes():
    return {"recipes": recipes}

@router.post("/recipes/")
def create_recipe(recipe: Recipe):
    recipe_dict = recipe.dict()
    recipes.append(recipe_dict)
    return {"recipe": recipe_dict, "status": "Recipe created"}

