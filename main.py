import flask
import os

import config
import api

app = flask.Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'secret_key'

# ---------------------------------------
# Routes
# ---------------------------------------

# Admin Routes Blueprints
# from routes.user.login import login_bp

# app.register_blueprint(login_bp)

# # College Admin Routes Blueprints
# from routes.admin.admin_events import admin_events_bp

# app.register_blueprint(admin_events_bp)


# ---------------------------------------
# 404 Error Handler
# ---------------------------------------

@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404


# ---------------------------------------
# Main
# ---------------------------------------

if __name__ == "__main__":
    app.run(port=4000, debug=True)