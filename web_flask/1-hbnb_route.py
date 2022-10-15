#!/usr/bin/python3
"""
A simple flask application
"""


from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """Returns Hello HBNB! from the given route"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns 'HBNB'"""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
