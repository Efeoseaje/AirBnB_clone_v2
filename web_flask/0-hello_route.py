#!/usr/bin/python3
"""0-hello_route module"""
import flask


app = flask.Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_HBNB():
    return "<p>Hello HBNB!</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=500)
