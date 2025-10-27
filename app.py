import os
from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def recipe_ideas(ingredients: list, num_recipes: int = 3) -> str:
    if not ingredients:
        return "Error: No ingredients provided."
    if num_recipes < 1:
        return "Error: Number of recipes must be at least 1."
    try:
        prompt = (
            f"You are a helpful assistant that suggests recipes.\n\n"
            f"Suggest {num_recipes} recipes using the following ingredients: "
            f"{', '.join(ingredients)}. "
            "For each recipe, provide its name and a list of key ingredients."
        )
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=500,
                temperature=0.7,
            )
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        ingredients_input = request.form.get("ingredients")
        num_recipes = int(request.form.get("num_recipes", 3))
        ingredients = [i.strip() for i in ingredients_input.split(",") if i.strip()]
        result = recipe_ideas(ingredients, num_recipes)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
