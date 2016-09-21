from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Gets a random quote
@app.route('/random')
def random_text():
    return jsonify(text="Once upon a time, the quick brown fox jumped over the lazy dog")

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

if __name__ == '__main__':
    app.run(debug=True)