# Import the library to create websites
from flask import Flask, render_template


app = Flask(__name__)


# Decorator Home Page
@app.route('/')
def home():
    return render_template("home.html")


# About Page
@app.route('/about')
def about():
    return render_template('about.html')


# Tanjil website
@app.route('/tanjil')
def tanjil():
    return render_template('main.html')


@app.route('/webmap')
def webmap():
    return render_template('world.html')

    

# Ignore the lines when import the app

if __name__ == '__main__':
    # Loads the website
    app.run(debug=True)
