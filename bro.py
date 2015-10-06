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
        'bruh',
        'bud',
        'buddy',
        'compadre',
        'dawg',
        'dood',
        'dude',
        'guy',
        'hermano',
        'homeboy',
        'homie',
        'mate',
        'm8',
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

@app.route('/<word>', strict_slashes=False)
def bro_me(word):
    if word in words:
        return jsonify({'bro': random.choice(words[word])})
    else:
        abort(404)

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not Found. Try one of /[bro|broette|nobro] instead'}), 404


if __name__ == '__main__':
    app.run()
