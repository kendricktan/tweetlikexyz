import os

from github_webhook import Webhook
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
webhook = Webhook(app, endpoint='/github-hook')

@app.route('/')
def index():
    return render_template('index.html')

# Gets a random quote
@app.route('/random')
def random_text():
    return jsonify(text="Once upon a time, the quick brown fox jumped over the lazy dog. And it tested its webhooks. Test 42")

# xyzfies your phrases
@app.route('/xyzfy', methods=['POST'])
def xyzfy_phrase():
    try:
        person = request.form.get('person')
        phrase = request.form.get('phrase')
        return jsonify(status="success")
    except ValueError:
        pass
    return jsonify(status="failed")

# Github webhook
@webhook.hook()
def on_github_push(data):
    os.system('../update.sh')

if __name__ == '__main__':
    app.run(debug=True)