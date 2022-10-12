class Item: 
    def __init__(self, id, name, status = 'To Do'): 
        self.id = id 
        self.name = name 
        self.status = status 

    @classmethod 
    def from_trello_card(cls, card, list): 
        return cls(card['id'], card['name'], list['name'])

    @classmethod
    def from_mongo_item(cls, mongo_item):
        return cls(mongo_item['_id'], mongo_item['task'], mongo_item['status'])