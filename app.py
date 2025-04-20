import flask

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def index():
    return flask.render_template('index.html')