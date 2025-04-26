from flask import Flask, render_template_string, request
import generativeai as genai

# Initialize the app
app = Flask(__name__)

# API key and model setup
API_KEY = "AIzaSyDls8P-uIJb5P-FBIPHZrcK03XlnJCFkOo"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-turbo")

# HTML template with embedded Flask templating
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generative AI Prompt</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
        }
        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
        }
        .response {
            margin-top: 20px;
            padding: 10px;
            background-color: #f1f1f1;
            border-radius: 5px;
            white-space: pre-wrap;
        }
        textarea {
            width: 100%;
            height: 150px;
            padding: 10px;
            margin-top: 10px;
            border-radius: 5px;
            border: 1px solid #ddd;
            resize: none;
        }
        button {
            padding: 10px 20px;
            margin-top: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Generative AI Prompt</h1>
        <form method="POST">
            <label for="user_prompt">Enter your prompt:</label>
            <textarea id="user_prompt" name="user_prompt" placeholder="Type your prompt here..." required></textarea>
            <button type="submit">Generate Response</button>
        </form>

        {% if response %}
        <div class="response">
            <h3>AI Response:</h3>
            <p>{{ response }}</p>
        </div>
        {% endif %}
    </div>

</body>
</html>
"""

# Route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = ""  # Default value for response
    if request.method == 'POST':
        # Get the prompt from the user input
        user_prompt = request.form['user_prompt']
        
        # Send the prompt to the model and get the response
        response = model.generate_content(user_prompt)
        response_text = response.text  # Assigning the response text from AI model

    # Return the response to the HTML template with the AI output
    return render_template_string(HTML_TEMPLATE, response=response_text)

if __name__ == '__main__':
    app.run(debug=True)
