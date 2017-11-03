import requests

# Use the access_template.py file to create your own access.py
from access import trello_access


def createBoard(boardname):
    
    url = "https://api.trello.com/1/boards/"
    querystring = {
        "name": {{cookiecutter.project_slug}},
        "key": trello_access["key"],
        "token": trello_access["token"]
    }
    response = requests.request("POST", url, params=querystring)
    print(response.text)

def main():
    pass

if __name__ == '__main__':
    main()