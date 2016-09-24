import os

#from models.lstm import get_rnn
from github_webhook import Webhook
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin

# Init our flask things
app = Flask(__name__)
CORS(app)
webhook = Webhook(app, endpoint='/github-hook')

# Our neural network for ...
print('[-] Loading shakespeare models...')
#model_shakespeare = get_rnn('model_shakespeare')
#model_shakespeare.load('models/model_shakespeare-192942')
print('[!] Finished loading models')

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

        if 'shakespeare' in person:
            return jsonify(xyzfy_phrase='to be or not to be, that is the question')

    except ValueError:
        pass
    return jsonify(status="failed")

# Github webhook
@webhook.hook()
def on_github_push(data):
    os.system('../update.sh')

if __name__ == '__main__':
    app.run(debug=True)