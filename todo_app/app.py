from flask import Flask, render_template, request
from todo_app.data.session_items import get_items, add_item

from todo_app.flask_config import Config 
import requests
import dotenv
import os


app = Flask(__name__)
app.config.from_object(Config())


@app.route('/', methods=['GET', 'POST'])
def index():

    url = "https://api.trello.com/1/boards/620a2eb50101820be8503973/"

    print(os.getenv("TRELLO_API_KEY"))

    querystring = {
    "key":os.getenv("TRELLO_API_KEY"),
    "token":os.getenv("TRELLO_API_TOKEN"),
    "cards": "open"
    }
    headers = {"content-type": "application/json"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    response_json = response.json()

    items = response_json['cards']

    return render_template('index.html', items = items)


@app.route('/todo', methods=['GET', 'POST']) 
def addItem(): 
        items = get_items()
        
        new_item = request.form.get('Todo')
        add_item(new_item)
        
       
        return index()
       