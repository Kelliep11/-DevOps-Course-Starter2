from flask import Flask, render_template, request, redirect

from todo_app.data.view_model import ViewModel

from todo_app.flask_config import Config 
import requests
import os
import todo_app.data.mongo_items as mongo_items
from flask_login import LoginManager, login_required, UserMixin, login_user, current_user

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config()) 

    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthenticated():
        redirect_url = f"https://github.com/login/oauth/authorize?client_id={os.getenv('CLIENT_ID')}"
        return redirect(redirect_url)

    @login_manager.user_loader
    def load_user(user_id):
            user = User(user_id)

            return user
    login_manager.init_app(app)    

    @app.route('/', methods=['GET', 'POST'])
    @login_required
    def index():
        items = mongo_items.get_items()    
        item_view_model = ViewModel(items)
        return render_template('index.html', view_model=item_view_model, user = current_user)      

    @app.route('/login/callback')
    def callback():
        authorisation_code = request.args['code']
        access_token_url = f"https://github.com/login/oauth/access_token"
        query_params = {
            "client_id": os.getenv('CLIENT_ID'),
            "client_secret": os.getenv('CLIENT_SECRET'),
            "code": authorisation_code
        }
        headers = {
            "Accept": "application/json"
        }
        access_token_response = requests.post(access_token_url, params = query_params, headers = headers)

        access_token = access_token_response.json()['access_token']

        user_info_url = 'https://api.github.com/user'

        auth_headers = {
            "Authorization": f"Bearer {access_token}"
        }
        
        user_info_response = requests.get(user_info_url, headers = auth_headers)
       
        id = user_info_response.json()['login']
        user = User(id)

        login_user(user)

        return redirect("/")

    class User(UserMixin): 
        def __init__(self, id): 
            self.id = id
          
            if id == 'Kelliep11':
                self.role = 'writer'
            else:
                self.role = 'reader' 
          


    @app.route('/todo', methods=['GET', 'POST']) 
    @login_required
    def addItem(): 
                
        if current_user.role == "reader":
            return "Forbidden", 403

        new_item_name = request.form.get('Todo')
        mongo_items.add_items(new_item_name)
        
        return index()
            
    @app.route('/complete_card', methods=['POST'])  
    @login_required     
    def complete_card():
                
        if current_user.role == "reader":
            return "Forbidden", 403

        card_id = request.form['card_id']
        mongo_items.complete_item(card_id) 
                 
        
        return index()
        


    return app





