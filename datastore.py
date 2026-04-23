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

class DataStore:
    _counter = 0

    def __init__(self):
        self.store = self._load()
        self._counter = self._findLargestId() + 1
        return
    
    def _itemExists(self, id):
        for index, item in enumerate(self.store):
            if item["id"] == int(id):
                return index
        return -1
    
    def _findLargestId(self):
        max = self.store[0]["id"] if self.store else None

        if max == None:
            return -1

        for item in self.store:
            if max < item["id"]:
                max = item["id"]
        
        return max
    
    def _save(self):
        with open("data.json", mode="w", encoding="utf-8") as file:
            json.dump(self.store, file)
        return
    
    def _load(self):
        try:
            with open("data.json", mode="r", encoding="utf-8") as file_stream:
                data = json.load(file_stream)
        except FileNotFoundError as err:
            logger.error("file error: data.json does not exist")
            return []
        
        return data
    
    def create(self, attr):
        item = {
            "id": self._counter,
            "attr": attr
        }
        self._counter += 1
        self.store.append(item)

        self._save()

        return
    
    def read(self):
        print(self.store)

        return
    
    def update(self, id, attr):
        index = self._itemExists(id)

        if index == -1:
            logger.warning("could not update, item does not exist")
            return
        
        self.store[int(id)]["attr"] = attr

        self._save()

        return
    
    def delete(self, id):
        index = self._itemExists(id)

        if index == False and index != 0:
            logger.warning("could not delete, item does not exist")
            return
        
        del self.store[index]

        logger.info("deleted item")

        self._save()

        return