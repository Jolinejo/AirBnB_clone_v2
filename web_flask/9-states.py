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


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def list_state(state_id=None):
    """list all states by name"""
    obj = list(storage.all(State).values())
    obj.sort(key=lambda x: x.name)
    found = False
    tgt = None
    if state_id is not None:
        for objs in obj:
            if objs.id == state_id:
                tgt = objs
                found = True
                break
    return render_template('9-states.html',
                           my_objects=obj, tgt=tgt, state_id=state_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
