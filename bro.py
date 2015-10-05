from flask import Flask, jsonify
import random

app = Flask(__name__)

words = ['amigo','bra','brah','bro','broski','brotha','brother','bud','buddy','compadre','dawg','dude','guy','homeboy','homie','mate','pal']

@app.route('/', methods=['GET'])
def root():
    return jsonify({'message': 'try /bro instead'})

@app.route('/bro', methods=['GET'])
def broMe():
    return jsonify({'bro': random.choice(words)})

@app.errorhandler(404)
def four04_error(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

if __name__ == '__main__':
    app.run()
