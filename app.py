import flask

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def home():
    return flask.render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, port=5080)