while True:
    userInput = input(
        '''
        Enter create, read, update, or delete.
        Enter quit to stop.
        '''
    ).lower()

    if userInput == "quit":
        break
    elif userInput == "create":
        print("user selected create")
    elif userInput == "read":
        print("user selected read")
    elif userInput == "update":
        print("user selected update")
    elif userInput == "delete":
        print("user selected delete")