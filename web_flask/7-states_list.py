#!/usr/bin/python3
"""script that starts a Flask web application"""
from models import storage
from flask import Flask, escape, render_template
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def closedb(stor):
    """Closes db session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_template():
    """function that route /states_list"""
    states = list(storage.all(State).values())
    states.sort(key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    storage.reload()
    app.run(host='0.0.0.0', port=5000, debug=True)
