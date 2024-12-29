from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'
        else:
            result = 'Invalid Operation'
        return render_template('index.html', result=result)
    except ValueError:
        return render_template('index.html', result="Invalid Input")

@app.route('/students')
def students():
    students_data = [
        {'name': 'Alice', 'roll_no': 101, 'preferred_language': 'Python'},
        {'name': 'Bob', 'roll_no': 102, 'preferred_language': 'Java'},
        {'name': 'Charlie', 'roll_no': 103, 'preferred_language': 'C++'}
    ]
    return render_template('students.html', students=students_data)

@app.route('/teachers')
def teachers():
    teachers_data = [
        {'name': 'Prof. Smith', 'module': 'Data Structures'},
        {'name': 'Dr. Brown', 'module': 'Machine Learning'},
        {'name': 'Ms. Johnson', 'module': 'Web Development'}
    ]
    return render_template('teachers.html', teachers=teachers_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
