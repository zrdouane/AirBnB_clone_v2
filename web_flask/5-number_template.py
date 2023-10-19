#!/usr/bin/python3
"""
script that starts a Flask web application
application must be listening on 0.0.0.0, port 5000.
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    /: display “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """
    /hbnb: display “HBNB”
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def Cvalue(text):
    """
    /c/<text>: display “C ” followed by the value of the
    text variable (replace underscore _ symbols  with a space )
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Pyvalue(text='is cool'):
    """
    display “Python ”, followed by the value of the text
    variable (replace underscore _ symbols with a space )
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def Numbervalue(n):
    """
    display “n is a number” only if n is an integer
    """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
