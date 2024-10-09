from flask import Flask, render_template, request, redirect, url_for
import openai

app = Flask(__name__)

# In-memory storage for protein logs
protein_logs = []

# OpenAI API configuration
openai.api_key = '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'

# Function to generate a fitness plan using OpenAI GPT
def generate_fitness_plan(height, weight, fitness_goal):
    # Mocked response
    return f"Sample fitness plan for height {height}, weight {weight}, and goal {fitness_goal}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form inputs
        height = request.form['height']
        weight = request.form['weight']
        fitness_goal = request.form['fitness_goal']
        
        # Generate fitness plan
        fitness_plan = generate_fitness_plan(height, weight, fitness_goal)
        
        return render_template('index.html', fitness_plan=fitness_plan)

    return render_template('index.html', fitness_plan=None)

@app.route('/log-protein', methods=['GET', 'POST'])
def log_protein():
    if request.method == 'POST':
        protein_amount = request.form['protein_amount']
        protein_logs.append(protein_amount)  # Simple in-memory storage

        return redirect(url_for('view_protein_logs'))

    return render_template('protein_log.html')

@app.route('/view-protein-logs')
def view_protein_logs():
    return render_template('protein_log.html', protein_logs=protein_logs)

if __name__ == '__main__':
    app.run(debug=True)