import datastore

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