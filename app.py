import flask

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def home():
    return flask.render_template('home.html')

@app.route('/login')
def login():
    return flask.render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return flask.render_template('dashboard.html')

@app.route('/colleges')
def colleges():
    return flask.render_template('colleges.html')

@app.route('/departments')
def departments():
    return flask.render_template('departments.html')

@app.route('/accounts')
def accounts():
    return flask.render_template('accounts.html')


if __name__ == '__main__':
    app.run(debug=True, port=5080)