from flask import session

def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
        
    """
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
    return session.get('items',)