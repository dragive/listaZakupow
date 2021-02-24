import json
from datetime import datetime
import random
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
    try:
        file = json.load(name)
    except Exception as ex:
        print(ex)
        return None
    return file
def outer(name="storage.json",storage:dict=init_file):
    json.dump(name,storage)


def execute(cmd=None):
    if cmd is None:
        return
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
def add(cmd=None):
    if cmd is not None or not len(cmd['args']) == 0:
        print(f'Args not supported')
        return
    type_item = input(f'Type of entry [CHARGE\Ch;Return/R;Comment/Co]: ')
    if type_item.lower() in ['ch','','charge','c']:
        type_item = 'Charge'
    elif type_item.lower() in ['r','rt','return','re','ret']:
        type_item = 'Return'
    elif type_item.lower() in ['co','comment','comm','cm']:
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
    STORAGE['Settings']['ID_next']+=1


def delete(cmd=None):
    if cmd is not None or not len(cmd['args']) == 0:
        print('Arguments not supported')
        return
    get_id = input('ID to be deleted: ')
    while True:
        try:
            get_id = int(get_id)
            if get_id <0 or get_id not in STORAGE["Storage"]['IDs']:
                raise Exception()
        except Exception as ex:
            get_id = input('Please insert correct ID: ')
            break
    ran = random.randint(1,5)
    print(f"To delete write {ran}: ",end='')
    print(end='Operation ')
    try:
        inp = int(input())
        if inp != ran:
            print(f"canceled")
            return
    except Exception as ex:
        print(f"canceled")
        return
    STORAGE['Storage']['IDs'].remove(get_id)
    STORAGE['Storage']['List'].pop(get_id)
    print('done')
    
def hide(cmd=None):
    if cmd is not None or not len(cmd['args']) == 0:
        print('Arguments not supported')
        return
    get_id = input('ID to be hided: ')
    while True:
        try:
            get_id = int(get_id)
            if get_id <0 or get_id not in STORAGE["Storage"]['IDs']:
                raise Exception()
        except Exception as ex:
            get_id = input('Please insert correct ID: ')
            break
    STORAGE['Storage']['List'][get_id]['Hidden']=True

def list_element(element,id,types='all'):
    if element is None or element['Hidden']==True:
        return
    if element('type_item') == 'Charge' and types in ('all','corech','ch','rech','coch'):
        print(f''' {id:4} | {element["Name"]:14.0} | {     element["Amount"]:5} | {element["Date"]:10.0} | {element["Desctription"]:20.0}''')
    elif element('type_item') == 'Comment' and types in ('all','corech','coch','core','co'):
        print(f''' {id:4} | {element["Name"]:14.0} | {''                    :5} | {element["Date"]:10.0} | {element["Desctription"]:20.0}''')
    elif element('type_item') == 'Return' and types in ('all','corech','rech','core','re'):
        print(f''' {id:4} | {element["Name"]:14.0} | {element["Amount"]*(-1):5} | {element["Date"]:10.0} | {element["Desctription"]:20.0}''')

def list_last(cmd=None,n=15):
    if cmd is not None or not len(cmd['args']) == 0:
        print('Arguments not supported')
        return
    l = STORAGE['Storage']['IDs']
    columns_to_be_print = []

    for i in STORAGE['Storage']['IDs']:
        if STORAGE['Storage']['List'][i]['Hidden']==False:
            columns_to_be_print.append(i)
            if len(columns_to_be_print) >=n:
                break
    columns_to_be_print = reversed(columns_to_be_print)
    for i in columns_to_be_print:
        list_element(STORAGE['Storage']['List'][i],i)

def unhide(cmd=None):
    if cmd is not None or not len(cmd['args']) == 0:
        print('Arguments not supported')
        return
    get_id = input('ID to be unhided: ')
    while True:
        try:
            get_id = int(get_id)
            if get_id <0 or get_id not in STORAGE["Storage"]['IDs']:
                raise Exception()
        except Exception as ex:
            get_id = input('Please insert correct ID: ')
            break
    STORAGE['Storage']['List'][get_id]['Hidden']=False

def command_not_found(cmd):
    print(f"Command not found: {cmd['oryginal']}")

def list_all(cmd=None):
    if cmd is not None or not len(cmd['args']) == 0:
        print('Arguments not supported')
        return
    l = STORAGE['Storage']['IDs']
    columns_to_be_print = []

    for i in STORAGE['Storage']['IDs']:
        if STORAGE['Storage']['List'][i]['Hidden']==False:
            columns_to_be_print.append(i)
            if len(columns_to_be_print) >=n:
                break
    columns_to_be_print = reversed(columns_to_be_print)
    for i in columns_to_be_print:
        list_element(STORAGE['Storage']['List'][i],i)

def print_help():
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