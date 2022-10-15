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

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    string = 'C'
    if '_' in text:
        texts  = text.split('_')
        new_str = ' '.join(texts)
        return '{} {}'.format(string, new_str)
    return string
        
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """ display “Python ”, followed by the value of the text parameter"""
    string = 'Python'
    if '_' in text:
        texts  = text.split('_')
        new_str = ' '.join(texts)
        return '{} {}'.format(string, new_str)
    return '{} {}'.format(string, text)

@app.route('/number/<int:n>',strict_slashes=False)
def is_int(n):
    """Checks if n is an integer"""
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
