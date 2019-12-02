import os
import requests
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'OPTIONS'])
def submit():
    action = request.args.get('action')
    if action not in ('Rock', 'Paper', 'Scissor'):
        return jsonify({'error': 'unknown action'})

    return jsonify(requests.get('http://' + os.getenv('BACK_IP'), verify=False, params={'action': action}).json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
