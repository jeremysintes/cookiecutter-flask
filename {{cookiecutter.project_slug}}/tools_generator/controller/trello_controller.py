import requests
import json

# Use the access_template.py file to create your own access.py
from access import trello_access


def createBoard(boardname):
    
    url = "https://api.trello.com/1/boards/"
    querystring = {
        "name": boardname,
        "key": trello_access["key"],
        "token": trello_access["token"]
    }
    response = requests.request("POST", url, params=querystring)

    print("Trello board created \n")
    with open('trello_detail.json', 'w') as td:
        json.dump(json.loads(response.text), td)

def closeBoard(trello_id):
    
    url = "https://api.trello.com/1/boards/%s" % (trello_id,)
    querystring = {
        "key": trello_access["key"],
        "token": trello_access["token"],
        "closed": "true"
    }
    response = requests.request("PUT", url, params=querystring)
    print(response.text)

def deleteBoard(trello_id):
    
    url = "https://api.trello.com/1/boards/%s" % (trello_id,)
    querystring = {
        "key": trello_access["key"],
        "token": trello_access["token"]
    }
    response = requests.request("DELETE", url, params=querystring)
    print(response.text)
    

def main():
    pass

if __name__ == '__main__':
    main()