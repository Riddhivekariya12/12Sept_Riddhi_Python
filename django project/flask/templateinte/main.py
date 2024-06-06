from flask import Flask
from flask import render_template

app= Flask(__name__,static_url_path='/static')

if __name__ == '__main__':
    app.run()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/404')
def errorpage():
    return render_template('404.html')

@app.route('/blog-single')
def blogsingle():
    return render_template('blog-single.html')

