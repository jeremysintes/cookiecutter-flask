import json
from controller import trello_controller
import os

def main():
    
    try:
        with open('trello_detail.json', 'r') as td:
            td = json.load(td)
            trello_id=td["id"]

        confirmation = "y"
        #confirmation = input("Are you sure you want to delete the board %s? (y/n)" % trello_id)
        
        if confirmation == "y":
            trello_controller.deleteBoard(trello_id)
            os.remove('trello_detail.json')
            print("Board destroyed ")
        else:
            print("The destroyer remain sleeping...")
    except:
        print("ERROR -- Trello not destroyed")
        pass


if __name__ == '__main__':
    main()


