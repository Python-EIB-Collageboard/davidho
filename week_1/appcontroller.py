import logging
import week_1.datastore as datastore

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler("system.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class AppController:
    def __init__(self):
        self.db = datastore.DataStore()
        return
    
    def run(self):
        while True:
            userInput = input(
                '''
    >>> Enter create, read, update, or delete.
    >>> Enter quit to stop.
                '''
            ).lower()
            if userInput == "quit":
                logger.info("user has quit program")
                break
            elif userInput == "create":
                logger.info("user selected create")
                attr = input("give an attribute for this item: ")
                self.db.create(attr)
            elif userInput == "read":
                logger.info("user selected read")
                self.db.read()
            elif userInput == "update":
                logger.info("user selected update")
                id = input("provide an ID: ")
                attr = input("provide an attribute: ")
                self.db.update(id, attr)
                pass
            elif userInput == "delete":
                logger.info("user selected delete")
                id = input("provide an ID: ")
                self.db.delete(id)
                pass
        
    

if __name__ == "__main__":
    appController = AppController()
    appController.run()