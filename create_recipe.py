import requests

api_url = "http://127.0.0.1:8000"

recipe_data = {
    "title": "Delicious Spaghetti Bolognese",
    "ingredients": "Spaghetti, Ground beef, Tomato sauce, Onion, Garlic",
    "steps": "1. Cook spaghetti; 2. Brown ground beef; 3. Saute onion and garlic; 4. Mix everything with tomato sauce"
}

response = requests.post(f"{api_url}/api/recipes/", json=recipe_data)

if response.status_code == 200:
    print("Recipe created successfully:")
    print(response.json())
else:
    print("Failed to create recipe. Status code:", response.status_code)
    print(response.text)
