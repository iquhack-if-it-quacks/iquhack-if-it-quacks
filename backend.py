import pickle
import random

from flask import Flask, render_template, request
from helper import *

app = Flask(__name__, template_folder='.', static_url_path='/', static_folder='.')

model = pickle.load(open("./classical-svc-model.pkl", 'rb'))


@app.route("/")
def index():
    return render_template('index.html')  # "Hello World!"


@app.route('/get_move', methods=['POST', 'GET'])
def get_move():
    req_board = request.json['board']
    req_turn = request.json['turn']
    grid = []
    for x in req_board:
        if x != 'X' and x != 'O':
            grid.append(0)
        else:
            grid.append(1 if x == req_turn else -1)
    for action in get_available_actions(grid):
        cgrid = grid.copy()
        cgrid[action] = 1
        cgrid = neutralize_grid(grid, -1)
        op_wins = model.predict([cgrid])[0]
        if not op_wins:
            return str(action)
    return str(random.choice(get_available_actions(grid)))


if __name__ == "__main__":
    app.run()
