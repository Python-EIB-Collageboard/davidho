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
        self.store = []
        return
    
    def _itemExists(self, id):
        for index, item in enumerate(self.store):
            if item["id"] == int(id):
                return index
        return -1
    
    # def _save(self):
    #     json_str = json.dumps({k: v.__dict__ for k,v in self.store.items()})

    #     with open("data.json", mode="w", encoding="utf-8") as file:
    #         file.write(json_str)
    #     return
    
    # def _load(self):
    #     try:
    #         with open("data.json", mode="r", encoding="utf-8") as file_stream:
    #             data = json.load(file_stream)
    #     except FileNotFoundError as err:
    #         logger.exception(f"file error: {err}")
    #         return {}
    #     return data
    
    def create(self):
        logger.info("user selected create")
        attr = input("give an attribute for this item: ")
        item = {
            "id": self._counter,
            "attr": attr
        }
        self._counter += 1
        self.store.append(item)
        return
    
    def read(self):
        logger.info("user selected read")
        print(self.store)
        # for item in self.store:
        #     print(item)
        return
    
    def update(self):
        logger.info("user selected update")
        id = input("provide an ID: ")
        index = self._itemExists(id)
        if index == -1:
            logger.warning("could not update, item does not exist")
            return
        attr = input("provide an attribute: ")
        self.store[int(id)]["attr"] = attr
        return
    
    def delete(self):
        logger.info("user selected delete")
        id = input("provide an ID: ")
        index = self._itemExists(id)
        if index == False and index != 0:
            logger.warning("could not delete, item does not exist")
            return
        del self.store[index]
        logger.info("deleted item")
        return