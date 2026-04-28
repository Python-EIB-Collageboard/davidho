class Item:
    id = 0

    def __init__(self, attr):
        self.id = Item.id
        self.attr = attr
        Item.id += 1

    def __str__(self):
        return "item with attr: " + self.attr

# my_item = Item()
# print(my_item.id)

# my_item1 = Item()
# print(my_item1.id)

def update(id, attr, collection):
    if id not in collection:
        print("could not update, item does not exist")
        return
    collection[id] = attr
    return

def delete(id, collection):
    if id not in collection:
        print("could not delete, item does not exist")
        return
    
    del collection[id]

collection = {}

while True:
    userInput = input(
        '''
    >>> Enter create, read, update, or delete.
    >>> Enter quit to stop.
        '''
    ).lower()

    if userInput == "quit":
        break
    elif userInput == "create":
        print("user selected create")
        attr = input("give an attribute for this item: ")
        item = Item(attr)
        collection[item.id] = item

    elif userInput == "read":
        print("user selected read")
        for id, item in collection.items():
            print(str(id) + ": ", item)
    elif userInput == "update":
        print("user selected update")
        id = input("provide an ID: ")
        attr = input("provide an attribute: ")
        update(int(id), attr, collection)
        print("updated " + str(id) +  " to have attribute of " + attr)
    elif userInput == "delete":
        print("user selected delete")
        id = input("provide an ID: ")
        delete(int(id), collection)