# 🍜 AI Recipe Generator (Flask + Gemini API)

This project is a simple web application built with Flask that generates recipe ideas based on ingredients you have at home, leveraging the Gemini API (`gemini-2.5-flash`) for intelligent content generation.

## ✨ Features

* **Recipe Suggestions:** Input a comma-separated list of ingredients and receive tailored recipe ideas.
* **Customizable Output:** Specify the number of recipes you want to generate (default is 3).
* **Simple Interface:** A clean, responsive design using Bootstrap 5 with a "glassmorphism" style effect.

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

* Python 3.8+
* A Google AI API Key (Get one from [Google AI Studio](https://ai.google.dev/))

## ⚙️ Setup and Installation

Follow these steps to get the project running locally.

### 1. Clone the repository

```bash
git clone <repository-url>
cd ai-recipe-generator
2. Create a Virtual Environment
It is highly recommended to use a virtual environment:

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows

**3.Install Dependencies**
Install the necessary Python packages using the provided requirements.txt:
pip install flask google-genai python-dotenv

4. Configure Environment Variables
Create a file named .env in the root directory of your project to store your API key securely:

.env file

# Replace YOUR_API_KEY_HERE with your actual Gemini API Key
GEMINI_API_KEY="YOUR_API_KEY_HERE"

🚀 Running the Application
Once setup is complete, you can run the application:
python app.py


The recipe generation is handled by the recipe_ideas function in app.py:

Python

# Initialization
model = genai.GenerativeModel('gemini-2.5-flash')

# Recipe Generation Function
def recipe_ideas(ingredients: list, num_recipes: int = 3) -> str:
    # ... (Error handling)
    prompt = (
        f"You are a helpful assistant that suggests recipes.\n\n"
        f"Suggest {num_recipes} recipes using the following ingredients: "
        f"{', '.join(ingredients)}. "
        # ... (further instructions)
    )
    response = model.generate_content(prompt, ...)
    return response.text
