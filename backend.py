import pickle
import random

import numpy as np
from flask import Flask, render_template, request
from helper import *

app = Flask(__name__, template_folder='.', static_url_path='/', static_folder='.')

# model1 = pickle.load(open("./quantum-svc-model01.pkl", 'rb'))
# model = pickle.load(open("./quantum-svc-model.pkl", 'rb'))
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

    op_not_win_move = None
    for action in get_available_actions(grid):
        cgrid = grid.copy()
        cgrid[action] = 1
        cgrid = neutralize_grid(cgrid, -1)
        res = model.predict(np.array([cgrid]))[0]
        print(cgrid, action, res)
        if res == -1:
            print('found win')
            return str(action)  # we win
        if res == 0:
            op_not_win_move = str(action)
        # res1 = model1.predict(np.array([cgrid]))[0]
        # if not res1:
        #     return str(action)
    if op_not_win_move is not None:
        return op_not_win_move
    print('didnt find')
    return str(random.choice(get_available_actions(grid)))


if __name__ == "__main__":
    app.run()
