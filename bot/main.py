import random
from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def generate_action():
    action = random.choice(['Rock', 'Paper', 'Scissor'])
    return jsonify({'action': action})


if __name__ == '__main__':
    app.run(port=5000)
