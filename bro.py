from flask import Flask, jsonify, abort
import random
import logging

app = Flask(__name__)

words = {
    'bro': [
        'amigo',
        'bra',
        'brah',
        'bro',
        'broski',
        'brotha',
        'brother',
        'broseph',
        'bud',
        'buddy',
        'compadre',
        'dawg',
        'dood',
        'dude',
        'guy',
        'homeboy',
        'homie',
        'mate',
        'man',
        'pal'
    ], 
    'broette': [
        'amiga',
        'babe',
        'bby',
        'bbygurl',
        'chica',
        'chick',
        'fembro',
        'gal',
        'girl',
        'girlbro',
        'girlfriend',
        'girlie',
        'gal',
        'homegirl',
        'lady',
        'sister',
        'sista',
        'woman'
    ],
    'nobro': [
        'associate',
        'bff',
        'chum',
        'consort',
        'fam',
        'friend',
        'friendo',
        'pal'
    ]
}

@app.route('/')
def root():
    return jsonify({'message': 'try /bro, /broette, or /nobro instead'})

@app.route('/<string:word>')
def bro_me(word):
    logging.warning("word is %s" % word)
    if word in words:
        return jsonify({'bro': random.choice(words[word])})
    else:
        abort(404)
        # return 'blah'

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not Found. Try one of /[bro|broette|nobro] instead'}), 404


if __name__ == '__main__':
    app.run()
