#!/usr/bin/python3
"""
A simple flask application
"""


from flask import Flask, render_template
from models.engine import db_storage as storage
from models import state
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def get_states():
    states = storage.all(state)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def get_cities():
    states = storage.all(state)
    return render_template('8-cities_by_states.html', states=states)

@app.route('/states/<id>')
def get_state(id):
    states = storage.all(state)
    state = None;
    for item in states:
        if item.id == id:
            state = item
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown():
    storage.close()
