from flask import Flask, render_template, request
from todo_app.data.session_items import get_items, add_item
from todo_app.data.trello_items import get_trello_items

from todo_app.flask_config import Config 
import requests
import os


app = Flask(__name__)
app.config.from_object(Config())


@app.route('/', methods=['GET', 'POST'])
def index():
        items = get_trello_items()

        return render_template('index.html', items = items)




@app.route('/todo', methods=['GET', 'POST']) 
def addItem(): 
        items = get_items()
        
        new_item = request.form.get('Todo')
        add_item(new_item)
        
       
        return index()
       