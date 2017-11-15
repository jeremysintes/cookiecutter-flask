import yaml
conf = yaml.safe_load(open("_config.yml"))


def main():
    if conf['trello'] == "y" :
        from controller import trello_controller 
        trello_controller.createBoard(conf['trello_board_name'])

if __name__ == '__main__':
    main()


