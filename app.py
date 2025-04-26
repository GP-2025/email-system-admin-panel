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
from routes.main import main_bp

app.register_blueprint(main_bp)


# ---------------------------------------
# Admin Routes Blueprints
# ---------------------------------------
from routes.admin.dashboard import admin_dashboard_bp
from routes.admin.colleges import admin_colleges_bp
# from routes.admin.departments import admin_departments_bp
# from routes.admin.accounts import admin_accounts_bp

app.register_blueprint(admin_dashboard_bp)
app.register_blueprint(admin_colleges_bp)
# app.register_blueprint(admin_departments_bp)
# app.register_blueprint(admin_accounts_bp)



# ---------------------------------------
# College Admin Routes Blueprints
# ---------------------------------------
from routes.college_admin.dashboard import college_admin_dashboard_bp
from routes.college_admin.departments import college_admin_departments_bp
from routes.college_admin.accounts import college_admin_accounts_bp

app.register_blueprint(college_admin_dashboard_bp)
app.register_blueprint(college_admin_departments_bp)
app.register_blueprint(college_admin_accounts_bp)


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