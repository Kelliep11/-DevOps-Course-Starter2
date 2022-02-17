from flask import Flask, render_template, request
from todo_app.data.session_items import get_items, add_item

from todo_app.flask_config import Config 
import requests
import os


app = Flask(__name__)
app.config.from_object(Config())


@app.route('/', methods=['GET', 'POST'])
def index():

    url = "https://api.trello.com/1/boards/620e338747c98f4449c740c7/lists"

    print(os.getenv("TRELLO_API_KEY"))

    querystring = {
    "key":os.getenv("TRELLO_API_KEY"),
    "token":os.getenv("TRELLO_API_TOKEN"),
    "cards":"open"
    }
    headers = {"content-type": "application/json"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    
    response_json = response.json()

    items = []

    for trello_list in response_json:
        for card in trello_list["cards"]:
            card["status"] = trello_list["name"]

    items = response_json[0]['cards']
    return render_template('index.html', items = items)


@app.route('/todo', methods=['GET', 'POST']) 
def addItem(): 
        items = get_items()
        
        new_item = request.form.get('Todo')
        add_item(new_item)
        
       
        return index()
       