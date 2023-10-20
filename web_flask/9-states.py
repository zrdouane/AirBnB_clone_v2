#!/usr/bin/python3
"""
script that starts a Flask web application.
web application must be listening on 0.0.0.0, port 5000.
must use storage for fetching data from the storage engine
(FileStorage or DBStorage) => from models import storage and storage.all(...)
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """
    display a HTML page: (inside the tag BODY).
    """
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """
    storage teardown
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
