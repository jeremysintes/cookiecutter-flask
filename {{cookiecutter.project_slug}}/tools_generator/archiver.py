import json
from controller import trello_controller

def main():
    with open('trello_detail.json', 'r') as td:
        td = json.load(td)
        trello_id=td["id"]

    trello_controller.closeBoard(trello_id)

if __name__ == '__main__':
    main()


