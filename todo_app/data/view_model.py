class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items
    
    @property
    def todo_items(self):
        filtered_items=[]
        for item in self._items:

            if item.status == "To Do":

                filtered_items.append(item)

        return filtered_items
        

    @property
    def done_items(self):
        filtered_items=[]
        for item in self._items:

            if item.status == "Done":

                filtered_items.append(item)

        return filtered_items