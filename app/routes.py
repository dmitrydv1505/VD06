from flask import render_template, request
from app import app

@app.route('/')
def index():
    return render_template('blog.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        hobby = request.form['hobby']
        age = request.form['age']
        return render_template('blog.html', name=name, city=city, hobby=hobby, age=age)
