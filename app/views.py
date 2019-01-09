from flask import render_template
from app import app
import random


@app.route('/')
@app.route('/index')

def index():
   """Index Page for Webapp"""
   special = {'num':random.randint(1,11), 'num2': random.randint(1,11)}
   numbers = [
        {
           'one': random.randint(1,50),
        
        
           'two': random.randint(1,50),
        
        
           'three': random.randint(1,50),
        
        
           'four': random.randint(1,50),
        
        
           'five': random.randint(1,50)
        }   
        ]
   #numbers = {'one':random.sample(range(50), 5)}
   return render_template('index.html', title='Home', numbers=numbers, special = special)



