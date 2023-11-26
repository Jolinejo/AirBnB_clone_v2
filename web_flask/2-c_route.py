#!/usr/bin/python3
"""
start flask module
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def main():
    """
    returning hello hbnb
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    returning hello hbnb
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_time(text):
    """
    returning hello hbnb
    """
    x = text.replace('_', ' ')
    st = "C " + x
    return st


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
