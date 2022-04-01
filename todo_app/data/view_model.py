class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items
    
    @property
    def todo_items(self):
        # TODO: Actually write the code!
        return []

    @property
    def done_items(self):
        return self._items