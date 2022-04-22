from flask import Flask, render_template, request
import os
import requests
import json
from todo_app.data.item import Item



def get_trello_items():
    url = f"https://api.trello.com/1/boards/{os.getenv('TRELLO_BOARD_ID')}/lists"

 
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
            my_item = Item.from_trello_card(card, trello_list)
            items.append(my_item)

    return items
    
def add_card(name):
    
    url = "https://api.trello.com/1/cards"

    querystring = {
        "key":os.getenv("TRELLO_API_KEY"),
        "token":os.getenv("TRELLO_API_TOKEN"),
        "name":name,
        "idList":"620e338c101c43271f9ac494"
    }

    headers = {"content-type": "application/json"}

    response = requests.request("POST", url, headers=headers, params=querystring)

    print(response.text)

def move_card_to_done(card_id):
    
    url = f"https://api.trello.com/1/cards/{card_id}" 

    querystring = {
        "key":os.getenv("TRELLO_API_KEY"),
        "token":os.getenv("TRELLO_API_TOKEN"),
        "idList":"620e33934c5aed55e2dd3fd5"}

    headers = {"content-type": "application/json"}

    response = requests.request("PUT", url, headers=headers, params=querystring)

    print(response.text)
    print(url)