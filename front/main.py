from flask import Flask
from flask import render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', USER_IP='http://user-service:5001')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
