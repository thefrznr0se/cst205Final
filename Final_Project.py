from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
import requests

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        origin = request.form['origin']
        destination = request.form['destination']

        route_info = get_route_info(origin, destination)
    
        return render_template('index.html', route_info=route_info, origin=origin, destination=destination)
    
    return render_template('index.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        origin = request.form['origin']
        destination = request.form['destination']

        route_info = get_route_info(origin, destination)

        return render_template('index.html', route_info=route_info, origin=origin, destination=destination)
    
    return render_template('index.html')


def get_route_info(origin, destination):
    api_key = "0ZOdZgHrvADP8FzwKEvjXVf8VCGLmUjy"
    base_url = "https://www.mapquestapi.com/directions/v2/route"

    params = {
        "key": api_key,
        "from": origin,
        "to": destination
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    return data['route']


app.run()