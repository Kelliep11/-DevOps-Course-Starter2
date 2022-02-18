from flask import Flask, render_template, request
import os
import requests
import json



def get_trello_items():
    url = "https://api.trello.com/1/boards/620e338747c98f4449c740c7/lists"

 
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
    return items
    
def add_card(name):
    
    url = "https://api.trello.com/1/cards"

    querystring = {"key":"19a37fc28f973a4171b9d117d7d8fdb3","token":"b1ed0521879b283013d0b50d044faf03aa5d07186455248929b07805d42c5593","name":name,"desc":"help card","idList":"620e338c101c43271f9ac494"}

    headers = {"content-type": "application/json"}

    response = requests.request("POST", url, headers=headers, params=querystring)

    print(response.text)
