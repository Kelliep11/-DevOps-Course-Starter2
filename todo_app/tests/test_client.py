import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app import app
import os
import requests
import json
import mongomock
import todo_app.data.mongo_items as mongo_items

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client




def test_index_page(monkeypatch, client):
    # Replace requests.request(url) with our own function
    mongo_items.add_items("Test card")

    # Make a request to our app's index page
    response = client.get('/')

    assert response.status_code == 200
    assert 'Test card' in response.data.decode()