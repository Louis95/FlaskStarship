from flask import Flask,  jsonify, request
from collections import ChainMap
import os
from utility import make_get_request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Welcome to FlaskStarship"

@app.route('/starships', methods=['GET'])
def get_starships():

    results = list()
    next_url = 'https://swapi.dev/api/starships/?page=1'
    
    while next_url:
        query_results = make_get_request(next_url)
        results.extend(query_results['results'])
        next_url = query_results['next']


    all_starships = {'starships':[], 'starships_unknown_hyperdrive':[]}

    for result in results:
        if result['hyperdrive_rating'] != 'unknown':
            all_starships['starships'].append({'name': result['name'], 'hyperdrive': float(result['hyperdrive_rating'])})
        else:
            all_starships['starships_unknown_hyperdrive'].append({'name': result['name']})
    
    all_starships['starships'] = sorted(all_starships['starships'], key=lambda k: k['hyperdrive'])


    return jsonify(all_starships)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)
