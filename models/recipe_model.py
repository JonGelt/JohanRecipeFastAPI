from pydantic import BaseModel

class Recipe(BaseModel):
    title: str
    ingredients: str
    steps: str