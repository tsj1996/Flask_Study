from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():    
    return render_template('index.html', current_title = 'Current Title')

@app.route('/about')
def about():
    return render_template('about.html')