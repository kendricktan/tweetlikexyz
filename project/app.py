from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Gets a random quote
@app.route('/random')
def random_text():
    return jsonify(text="Once upon a time, the quick brown fox jumped over the lazy dog")

# xyzfies your phrases
@app.route('/quote', methods=['POST'])
def xyzfy_phrase():
    return jsonify(text="hello")

if __name__ == '__main__':
    app.run(debug=True)