#!/usr/bin/python3
"""
start flask module
"""


from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    """remove session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_state():
    """list all states by name with cities"""
    my_objects = list(storage.all(State).values())
    my_objects.sort(key=lambda x: x.name)
    return render_template('8-cities_by_states.html', my_objects=my_objects)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
