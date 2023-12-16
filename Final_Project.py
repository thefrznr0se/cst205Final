from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from user_info import user_info
import requests

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/', methods=['GET', 'POST'])
@app.route("/", methods=('GET', 'POST'))
def test():
    if request.method == "POST":
        user = request.form['username']
        password = request.form['Password']

        size = len(user_info)
        for x in range(size):
            if user_info[x]['username'] == user and user_info[x]['password'] == password:
                return render_template('index.html')

    return render_template('login.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    # Handle POST request data
    if request.method == 'POST':
        origin = request.form['origin']
        destination = request.form['destination']
        # Perform some processing, possibly with functions like get_route_info and get_route_info2
        route_info = get_route_info(origin, destination)
        static_map_url = get_route_info2(origin, destination)
        # Render the 'index.html' template with the processed data
        return render_template('index.html', route_info=route_info, static_map_url=static_map_url, origin=origin, destination=destination)
    
    return render_template('index.html')


@app.route('/index2', methods=['GET', 'POST'])
def index2():
    if request.method == 'POST':
        # Get user input from the form
        origin = request.form['origin']
        destination1 = request.form['destination1']
        destination2 = request.form['destination2']
        destination3 = request.form['destination3']

        # Get the route information from MapQuest API
        route_info = get_route_info(origin, destination1)
        route_info1 = get_route_info(origin, destination2)
        route_info2 = get_route_info(origin, destination3)

        # Get the static map URL
        static_map_url = get_route_info2(origin, destination1)
        static_map_url1 = get_route_info2(origin, destination2)
        static_map_url2 = get_route_info2(origin, destination3)

   

        return render_template('index2.html', route_info=route_info, route_info1=route_info1, route_info2=route_info2, static_map_url=static_map_url, origin=origin,
         destination1=destination1, destination2=destination2, destination3=destination3,
         static_map_url1=static_map_url1, static_map_url2=static_map_url2)
    #Render the 'index.html' template for GET requests
    return render_template('index2.html')


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

def get_route_info2(origin, destination):
    return 'https://mapquestapi.com/staticmap/v5/map?start=' + f'{origin}' + '|flag-start&end=' + f'{destination}' +  '|flag-end&type=dark&size=1000,400@2x&traffic=flow|cons|&key=0ZOdZgHrvADP8FzwKEvjXVf8VCGLmUjy'

@app.route('/create_account', methods=('GET', 'POST'))
def create_account():
    if request.method == "POST":
        user = request.form['username']
        password = request.form['Password']

        user_info.append({
        'username': user,
        'password': password
        })
        
        return render_template('login.html')

    return render_template('create_account.html')