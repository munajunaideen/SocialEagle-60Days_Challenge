from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Math API! Use /add, /subtract, /multiply, or /divide."})

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    result = data['a'] + data['b']
    return jsonify({"operation": "addition", "result": result})

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    result = data['a'] - data['b']
    return jsonify({"operation": "subtraction", "result": result})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    result = data['a'] * data['b']
    return jsonify({"operation": "multiplication", "result": result})

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    if data['b'] == 0:
        return jsonify({"error": "Division by zero is not allowed!"}), 400
    result = data['a'] / data['b']
    return jsonify({"operation": "division", "result": result})

if __name__ == '__main__':
    app.run(debug=True)
