#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Route /cities_by_states
    Displays a HTML page
        - 'H1' tag: "States"
        - 'UL' tag: with the list of all 'State' objects present in DBStorage
          sorted by name (A->Z)
            - 'LI' tag: description of one 'State': <state.id>: <B><state.name>
              </B> + 'UL' tag: with the list of 'City' objects linked to the
              'State' sorted by name (A->Z)
                - 'LI' tag: description of one 'City': <city.id>:
                  <B><city.name></B>
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template("8-cities_by_states.html", states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
