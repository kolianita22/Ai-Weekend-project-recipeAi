import os
from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API client with the API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel('gemini-1.5-flash') 

def recipe_ideas(ingredients: list, num_recipes: int = 3) -> str:
    
    if not ingredients:
        return "Error: No ingredients provided."
    if num_recipes < 1:
        return "Error: Number of recipes must be at least 1."

    try:
        # Construct the prompt for the Gemini model
        prompt = (
            f"You are a helpful assistant that suggests recipes.\n\n"
            f"Suggest {num_recipes} recipes using the following ingredients: "
            f"{', '.join(ingredients)}. "
            "For each recipe, provide its name and a list of key ingredients."
        )

        # Make the API call to Gemini
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=500,
                temperature=0.7,
            )
        )

        # Access the generated text from the response
        return response.text

    except Exception as e:
        # Catch any exceptions that occur during the API call or processing
        return f"Error: {str(e)}"

if __name__ == "__main__":
    ingredients = ["chicken", "rice", "broccoli"]
    print("Recipe Ideas:")
    print(recipe_ideas(ingredients, num_recipes=2))

    print("\n---")
    ingredients_2 = ["tomato", "pasta", "garlic", "basil"]
    print("Recipe Ideas for Tomato, Pasta, Garlic, Basil:")
    print(recipe_ideas(ingredients_2, num_recipes=3))

    print("\n---")
    print("Testing error handling (no ingredients):")
    print(recipe_ideas([], num_recipes=1))

    print("\n---")
    print("Testing error handling (invalid num_recipes):")
    print(recipe_ideas(["egg"], num_recipes=0))
