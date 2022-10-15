#!/usr/bin/python3
"""
A simple flask application
"""


from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_BNB():
    """Returns Hello HBNB! from the given route"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
