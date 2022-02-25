from flask import Flask, render_template, request
from todo_app.data.trello_items import get_trello_items, add_card, move_card_to_done

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
                
        new_item_name = request.form.get('Todo')
        add_card(new_item_name)
        
       
        return index()


@app.route('/complete_Card', methods=['POST'])       
def complete_Card():
        card_id = request.form['card_id']
        move_card_to_done(card_id)
                
        return index()
        
    