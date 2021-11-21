from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login.html')
def login():
    return render_template('login.html')
    
@app.route('/courses.html')
def courses():
    return render_template('courses.html', course = ["AP Chemistry","AP Biology","AP Physics C","Honors Physics","Honors Chemistry","Honors Biology", "Physics"], hours = 6, student = ["Noah","Sam","Antong"], assignments = ["Theology Googlesite [2hours]", "Physics Simulation [3hours]", "Soccer Practice [4hours]"])

@app.route('/assignment.html')
def assignment():
    return render_template('assignment.html') 

if __name__ == '__main__':
   app.run(debug=True)

