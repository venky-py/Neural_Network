from flask import Flask, render_template

app = Flask(__name__)

# Sample data for students
students = [
    {"name": "John Doe", "roll_no": 101, "language": "Python"},
    {"name": "Jane Smith", "roll_no": 102, "language": "JavaScript"},
    {"name": "Michael Brown", "roll_no": 103, "language": "C++"},
    {"name": "Emily Davis", "roll_no": 104, "language": "Java"},
    {"name": "David Wilson", "roll_no": 105, "language": "Ruby"}
]

@app.route('/')
def index():
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)