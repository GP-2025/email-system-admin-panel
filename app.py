import flask
import os

import config
import api

app = flask.Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'secret_key'

# ---------------------------------------
# Main Routes Blueprints
# ---------------------------------------
from routes.main.get_started import get_started_bp
from routes.main.home import home_bp
from routes.main.login import login_bp

app.register_blueprint(get_started_bp)
app.register_blueprint(home_bp)
app.register_blueprint(login_bp)


# ---------------------------------------
# Admin Routes Blueprints
# ---------------------------------------



# ---------------------------------------
# College Admin Routes Blueprints
# ---------------------------------------



# ---------------------------------------
# 404 Error Handler
# ---------------------------------------

@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('/main/en/404.html'), 404


# ---------------------------------------
# Main
# ---------------------------------------

if __name__ == "__main__":
    app.run(port=4000, debug=True)