from flask import Flask
from flask import render_template,redirect
import random

app = Flask(__name__)


@app.route('/')
def index():
    nm="riddhi"
    num=random.randint(1111,9999)
    return render_template('index.html',name=nm,num=num,)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
