import flask
import os

import config
import api

app = flask.Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'secret_key'


# ---------------------------------------
# test
# ---------------------------------------

@app.route("/test")
def test():
    return flask.render_template('/test.html')


# ---------------------------------------
# Main Routes Blueprints
# ---------------------------------------
from routes.main.home import home_bp
from routes.main.login import login_bp
from routes.main.admin import admin_bp

app.register_blueprint(home_bp)
app.register_blueprint(login_bp)
app.register_blueprint(admin_bp)


# ---------------------------------------
# Admin Routes Blueprints
# ---------------------------------------



# ---------------------------------------
# College Admin Routes Blueprints
# ---------------------------------------

from routes.college_admin.dashboard import college_admin_dashboard_bp

app.register_blueprint(college_admin_dashboard_bp)


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