from flask import Flask, render_template
import main

app = Flask(__name__)


@app.route('/', methods=['GET'])
def mains():

    main.shuffler()
    initialState = main.initial_state
    print initialState
    main.bfs(initialState)
    moves = main.backtrace()
    print moves

    return render_template('front.html', first=initialState, moves=moves)

app.run(debug=True)
