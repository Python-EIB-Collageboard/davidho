class Item:
    id = 0

    def __init__(self, attr):
        self.id = Item.id
        self.attr = attr
        Item.id += 1

    def __str__(self):
        return "item with attr: " + self.attr
    
    def update(self, attr):
        self.attr = attr
        return

class DataStore:

    def __init__(self):
        self.store = {}
        return
    
    def _itemExists(self, id):
        if id in self.store:
           return True
        return False
    
    def create(self):
        print("user selected create")
        attr = input("give an attribute for this item: ")
        item = Item(attr)
        self.store[item.id] = item
        return
    
    def read(self):
        print("user selected read")
        for id, item in self.store.items():
            print(str(id) + ": ", item)
        return
    
    def update(self):
        print("user selected update")
        id = input("provide an ID: ")
        if not self._itemExists((int(id))):
            print("could not update, item does not exist")
            return
        attr = input("provide an attribute: ")
        self.store[int(id)].update(attr)
        return
    
    def delete(self):
        print("user selected delete")
        id = input("provide an ID: ")
        if not self._itemExists(int(id)):
            print("could not delete, item does not exist")
            return
        del self.store[int(id)]
        print("deleted item")
        return