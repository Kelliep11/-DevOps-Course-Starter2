from flask import Flask, render_template, request
import os
import requests

url = "https://api.trello.com/1/boards/620e338747c98f4449c740c7/lists"

 
querystring = {
    "key":os.getenv("TRELLO_API_KEY"),
    "token":os.getenv("TRELLO_API_TOKEN"),
    "cards":"open"
    }
headers = {"content-type": "application/json"}

response = requests.request("GET", url, headers=headers, params=querystring)

def get_trello_items():
    
    response_json = response.json()

    items = []

    for trello_list in response_json:
        for card in trello_list["cards"]:
            card["status"] = trello_list["name"]

    items = response_json[0]['cards']
    return items
    