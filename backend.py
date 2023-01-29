import flask
from flask import Flask, render_template

app = Flask(__name__, template_folder='.', static_url_path='/', static_folder='.')


@app.route("/")
def hello_world():
    return render_template('index.html')  # "Hello World!"


# @app.GET("/get_move")
# def hello_world():
#     return render_template('index.html')  # "Hello World!"


if __name__ == "__main__":
    app.run()
