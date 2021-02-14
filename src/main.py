import json
from datetime import datetime
init_file={
    'Settings':
        {"ID_next": 0,
        'Language': 'Eng',
        'Version':0.1},
    'Storage': {
        'IDs':[0],
        'List':{
        }
    }

}

STORAGE={}
def parser(name="storage.json"):
    file = json.load(name)
    return file
def outer(name="storage.json",storage:dict=init_file):
    json.dump(name,storage)


def execute(cmd):
    '''
    cmd = {
    'type':
    'oryginal':
    'args':[]
    }
    '''
    if cmd['type'] == "add":
        add(cmd)
    elif cmd['type'] == "delete":
        delete(cmd)
    elif cmd['type'] == "hide":
        hide(cmd)
    elif cmd['type'] == "list":
        list_last(cmd)
    elif cmd['type'] == "unhide":
        unhide(cmd)
    elif cmd['type'] == "list_all":
        list_all()
    elif cmd['type'] == "help":
        print_help()
    else:
        command_not_found(cmd)
def add(cmd):
    if len(cmd['args']) >1:
        print(f'Args not supported')
        return
    type_item = input(f'Type of entry [CHARGE\CH;Return/R;Comment/Co]: ')
    if type_item.lower() in ['ch','','charge','c']:
        type_item = 'Charge'
    elif type_item.lower() in ['r','rt','return']:
        type_item = 'Return'
    elif type_item.lower() in ['co','comment','comm']:
        type_item = 'Comment'
    name = input(f'What was bought: ')
    desc = input(f'Description: ')
    date = input(f'Date: ')
    if date == '':
        date = datetime.today().strftime('%Y-%m-%d')
    amount = input('Amount: ')
    while True:
        try:
            amount = float(amount)
        except Exception as ex:
            amount = input('Please insert correct amount: ')
            continue
        break
    hidden = False
 
    STORAGE['Storage']['IDs'].append(STORAGE['Settings']['ID_next'])
    STORAGE['Storage']['List'][STORAGE['Settings']['ID_next']] = {
        'Type':type_item,'Name':name, 
        'Desctription':desc,'Date':date,
        'Amount':amount,'Hidden':hidden

    }


def print_help():
    pass

def delete(cmd):
    pass

def hide(cmd):
    pass

def list_last(cmd):
    pass

def unhide(cmd):
    pass

def command_not_found(cmd):
    print(f"Command not found: {cmd['oryginal']}")

def list_all():
    pass


def execute_lst(cmd_list):
    return [execute(cmd) for cmd in cmd_list]
        



{
    'Settings':
        {"ID_next": 1,
        'Language': 'Eng',
        'Version':0.1},
    'Storage': {
        'IDs':[0],
        'List':{
            0: {'Type':'Charge','Name':'TEST NAME TEST', 
                'Desctription':'Lorem ipsum et ####','Date':'2137-04-24',
                'Amount':420,'Hidden':False}
        }
    }

}