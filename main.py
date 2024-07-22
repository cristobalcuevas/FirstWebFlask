from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'


@app.route('/route')
def route():
    return 'Hello from new route!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
