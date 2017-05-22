#flask rest service
from flask import Flask, jsonify, make_response, abort, request
from algorithems.svd import SupportVectorMachine

app = Flask(__name__)


def setup(app):
    svd = SupportVectorMachine()
    try:
        svd.load()
    except Exception as e:
        app.logger.error(e.message)
    app.config['SVD'] = svd
setup(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.route('/api/v1.0/plaintext', methods=['POST'])
def create_task():
    """
    Run this file and test it with:
    curl -i -H "Content-Type: application/json" -X POST -d '{"text":"This movie is bad!"}' http://127.0.0.1:5000/api/v1.0/plaintext
    """
    if not request.json or not 'text' in request.json:
        abort(400)
    try:
        result = app.config['SVD'].predict(request.json['text'])
    except Exception as e:
        return make_response(jsonify({'error': e.message}), 503)
    payload = {
        'text': request.json['text'],
        'positive': (True if result == 1 else False)
    }
    return jsonify(payload), 201

if __name__ == '__main__':
    app.run(debug=True)