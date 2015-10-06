from flask import Flask, jsonify
import random

app = Flask(__name__)

browords = ['amigo','bra','brah','bro','broski','brotha','brother','broseph','bud','buddy','compadre','dawg','dood','dude','guy','homeboy','homie','mate','man','pal']
broettewords = ['amiga','babe','bby','bbygurl','chica','chick','fembro','gal','girl','girlbro','girlfriend','girlie','gal','homegirl','lady','sister','sista','woman']
nowords = ['associate','bff','chum','consort','fam','friend','friendo','pal']

@app.route('/', methods=['GET'])
def root():
    return jsonify({'message': 'try /bro, /broette, or /nobro instead'})

@app.route('/bro', methods=['GET'])
def broMe():
    return jsonify({'bro': random.choice(browords)})

@app.route('/broette', methods=['GET'])
def broMe():
    return jsonify({'bro': random.choice(broettewords)})

@app.route('/nobro', methods=['GET'])
def broMe():
    return jsonify({'bro': random.choice(nowords)})

@app.errorhandler(404)
def four04_error(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

if __name__ == '__main__':
    app.run()
