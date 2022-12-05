#!/usr/bin/python3


"""start the Flask Web application by"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """return a string from route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return a string from hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """return a string from c /text"""
    return "C " + text.replace("_", " ")


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    """return a string from python/text"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def if_number(n):
    """return a string from number/n"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:num>', strict_slashes=False)
def to_display_html(num):
    """return a HTML page only if n is an integer:"""
    return render_template('5-number.html', num=num)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
