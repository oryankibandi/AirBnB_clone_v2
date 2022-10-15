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


@app.teardown_appcontext
def teardown():
    storage.close()
