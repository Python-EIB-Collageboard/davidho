import json
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler("system.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class Item:
    _counter = 0

    def __init__(self, attr):
        self.id = Item._counter
        self.attr = attr
        Item._counter += 1

    def __str__(self):
        return "item with attr: " + self.attr
    
    def update(self, attr):
        self.attr = attr
        return

class DataStore:

    def __init__(self):
        self.store = self._load()
        return
    
    def _itemExists(self, id):
        if id in self.store:
           return True
        return False
    
    def _save(self):
        json_str = json.dumps({k: v.__dict__ for k,v in self.store.items()})

        with open("data.json", mode="w", encoding="utf-8") as file:
            file.write(json_str)
        return
    
    def _load(self):
        try:
            with open("data.json", mode="r", encoding="utf-8") as file_stream:
                data = json.load(file_stream)
        except FileNotFoundError as err:
            logger.exception(f"file error: {err}")
            return {}
        return data
    
    def create(self):
        logger.info("user selected create")
        attr = input("give an attribute for this item: ")
        item = Item(attr)
        self.store[item.id] = item

        self._save()
        return
    
    def read(self):
        logger.info("user selected read")
        for id, item in self.store.items():
            logger.info(str(id) + ": ", item)
        return
    
    def update(self):
        logger.info("user selected update")
        id = input("provide an ID: ")
        if not self._itemExists((int(id))):
            logger.warning("could not update, item does not exist")
            return
        attr = input("provide an attribute: ")
        self.store[int(id)].update(attr)
        return
    
    def delete(self):
        logger.info("user selected delete")
        id = input("provide an ID: ")
        if not self._itemExists(int(id)):
            logger.warning("could not delete, item does not exist")
            return
        del self.store[int(id)]
        logger.info("deleted item")
        return