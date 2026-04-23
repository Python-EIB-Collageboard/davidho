import logging
import datastore

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
                self.db.create()
            elif userInput == "read":
                self.db.read()
            elif userInput == "update":
                self.db.update()
                pass
            elif userInput == "delete":
                self.db.delete()
                pass
        
    

if __name__ == "__main__":
    appController = AppController()
    appController.run()