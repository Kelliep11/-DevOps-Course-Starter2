from flask import Flask, render_template, request
from todo_app.data.trello_items import get_trello_items, add_card, move_card_to_done
from todo_app.data.view_model import ViewModel

from todo_app.flask_config import Config 
import requests
import os
import todo_app.data.mongo_items as mongo_items

def create_app():
        app = Flask(__name__)
        app.config.from_object(Config()) 
        @app.route('/', methods=['GET', 'POST'])
        def index():
                items = mongo_items.get_items()

                item_view_model = ViewModel(items)
                return render_template('index.html', view_model=item_view_model)  
        @app.route('/todo', methods=['GET', 'POST']) 
        def addItem(): 
                new_item_name = request.form.get('Todo')
                mongo_items.add_items(new_item_name)
                return index()
        @app.route('/complete_Card', methods=['POST'])       
        def complete_Card():
                card_id = request.form['card_id']
                move_card_to_done(card_id)  
                return index()
        return app





