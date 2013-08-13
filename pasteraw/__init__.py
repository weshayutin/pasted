import flask
from raven.contrib.flask import Sentry


app = flask.Flask(__name__, instance_relative_config=True)

# start with a default configuration
app.config.from_object('pasteraw.config')

# override defaults with instance-specific configuration
app.config.from_pyfile('pasteraw_config.py', silent=True)

# provide error notifications
sentry = Sentry(app)


import pasteraw.views  # flake8: noqa
