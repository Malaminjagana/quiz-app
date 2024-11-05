# app.py
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

questions = [
    {"question": "What is the capital of Gambia?", "options": ["London", "Berlin", "Paris", "Madrid"], "answer": "Banjul"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "What is the color of the sky on a clear day?", "options": ["Green", "Blue", "Red", "Yellow"], "answer": "Blue"},
    {"question": "What is the largest planet in our Solar System?", "options": ["Mars", "Earth", "Jupiter", "Saturn"], "answer": "Jupiter"},
    {"question": "Who wrote 'Hamlet'?", "options": ["Shakespeare", "Hemingway", "Twain", "Dickens"], "answer": "Shakespeare"},
    {"question": "What is the square root of 64?", "options": ["6", "7", "8", "9"], "answer": "8"},
    {"question": "Which element has the chemical symbol 'O'?", "options": ["Oxygen", "Gold", "Iron", "Silver"], "answer": "Oxygen"},
    {"question": "How many continents are there?", "options": ["5", "6", "7", "8"], "answer": "7"},
    {"question": "What is the boiling point of water in Celsius?", "options": ["90°C", "95°C", "100°C", "110°C"], "answer": "100°C"},
    {"question": "What is the longest river in the world?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], "answer": "Nile"},
    {"question": "In which country is the Great Wall located?", "options": ["India", "China", "Japan", "Korea"], "answer": "China"},
    {"question": "What is H2O commonly known as?", "options": ["Oxygen", "Hydrogen", "Water", "Salt"], "answer": "Water"},
    {"question": "Who painted the Mona Lisa?", "options": ["Da Vinci", "Picasso", "Van Gogh", "Rembrandt"], "answer": "Da Vinci"},
    {"question": "What planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe", "Shark"], "answer": "Blue Whale"},
    {"question": "What gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
    {"question": "Who is known as the father of physics?", "options": ["Newton", "Einstein", "Galileo", "Tesla"], "answer": "Newton"},
    {"question": "How many legs does a spider have?", "options": ["6", "8", "10", "12"], "answer": "8"},
    {"question": "What is the main ingredient in guacamole?", "options": ["Tomato", "Avocado", "Pepper", "Lettuce"], "answer": "Avocado"},
    {"question": "In what year did World War II end?", "options": ["1940", "1945", "1950", "1960"], "answer": "1945"},
]

# Route to serve the main quiz page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to get quiz questions
@app.route('/api/questions', methods=['GET'])
def get_questions():
    return jsonify(questions)

# API endpoint to check answers
@app.route('/api/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    question_index = data.get("question_index")
    answer = data.get("answer")

    correct_answer = questions[question_index]["answer"]
    return jsonify({"correct": answer == correct_answer})

if __name__ == '__main__':
    app.run(debug=True)
