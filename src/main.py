#!/usr/bin/python3
import json
from datetime import datetime
import random
import logging 
from debug import *
import os, sys
DEBUG = True
start_date = datetime.today().strftime('%Y-%m-%d %H-%M-%S')
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',filename=f'logs/run {start_date}.log')
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
# log.setLevel(log.DEBUG)


init_file={
    'Settings':
        {"ID_next": 0,
        'Language': 'Eng',
        'Version':1.0},
    'Storage': {
        'IDs':[],
        'List':{
        }
    }
}


Reminders = []
Storage={}
def parser(name="storage.json"):
    global Storage
    if DEBUG: 
        if Storage == {}:
                Storage = get_INIT_DEBUG_FILE()
        return 
    
    try:
        with open(name) as file:
            log.debug(f'opened file {name}')
            value = json.load(file)
    except Exception as ex:
        log.debug(f'Exception in parser')
        Storage = init_file
        return 
    Storage =  value

def outer(name="storage.json"):
    log.debug(f'Started outer')
    with open(name,'w+') as file:
        json.dump(Storage, file)
    log.debug(f'Ended outer')

def execute(cmd=None):
    log.debug(f'Started Execute functions')
    if cmd is None:
        log.debug(f'Cmd is None')
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
        list_all(cmd)
    elif cmd['type'] == "help":
        print_help(cmd)
    elif cmd['type'] == 'summary':
        summary()
    else:
        command_not_found(cmd)

def add(cmd=None):
    log.debug(f'Started Add function')
    if cmd is None or not len(cmd['args']) == 0:
        print(f'Args not supported')
        log.debug(f'Args not supported')
        return
    log.debug(f'Started form in add function')
    type_item = input(f'Type of entry [CHARGE\Ch;Return/R;Comment/Co]: ')
    while True:
        if type_item.lower() in ['ch','','charge','c']:
            type_item = 'Charge'
        elif type_item.lower() in ['r','rt','return','re','ret']:
            type_item = 'Return'
        elif type_item.lower() in ['co','comment','comm','cm']:
            type_item = 'Comment'
        else:
            print(f'Please insert correct value',end='')
            type_item = input(f'Type of entry [CHARGE\Ch;Return/R;Comment/Co]: ')
            continue
        break

    name = input(f'Title: ')
    desc = input(f'Description: ')
    date = input(f'Date: ')
    if date == '':
        date = datetime.today().strftime('%Y-%m-%d')
    if type_item not in ('Comment'):
        amount = input('Amount: ')
        while True:
            try:
                amount = float(amount)
            except Exception as ex:
                amount = input('Please insert correct amount: ')
                continue
            break
    hidden = False
    log.debug(f'End of form in add function')
    Storage['Storage']['IDs'].append(str(Storage['Settings']['ID_next']))
    if type_item not in ('Comment'):
        Storage['Storage']['List'][Storage['Settings']['ID_next']] = {
        'Type':type_item,'Name':name, 
        'Description':desc,'Date':date,
        'Amount':amount,'Hidden':hidden
    }
    else: 
        Storage['Storage']['List'][Storage['Settings']['ID_next']] = {
        'Type':type_item,'Name':name, 
        'Description':desc,'Date':date,
        'Hidden':hidden
    }
    Storage['Settings']['ID_next']+=1

def add_budget(cmd = None):
    log.debug(f'Started add_budget function')
    if cmd is None or not len(cmd['args']) == 0:
        print(f'Args not supported')
        log.debug(f'Args not supported')
        return
    log.debug(f'Started form in add_budget function')
    id = get_random_id(Storage['Storage']["Budgets"]['_'])

    title = input(f'Title: ')
    desc = input(f'Description: ')
    date = datetime.today().strftime('%Y-%m-%d')

    minimum = input('Put lower bound when the notyfication will appear\nor leave blank for no constraint: ')
    while True:
        try:
            if minimum == '':
                minimum = None
                break
            minimum = float('.'.join(minimum.split(',')))
            break
        except:
            minimum = input('Place correct number or leave empty: ')

    maximum = input('Put higher bound when the notyfication will appear\nor leave blank for no constraint: ')
    while True:
        try:
            if maximum == '':
                maximum = None
                break
            maximum = float('.'.join(maximum.split(',')))
            break
        except:
            maximum = input('Place correct number or leave empty: ')

    hidden = False
    log.debug(f'End of form in add_budget function')
    Storage['Storage']["Budgets"]['_'].append(id)
    Storage['Storage']["Budgets"][id] = {
        "Title": title,
        "Description": desc,
        "IncludeBudgets":[],
        "Reminders": [minimum, maximum],
        "DateOfCreation":date,
        "Hidden": hidden,
        "LoT": [] 
    }
    

'''
{
    'Settings':
        {"ID_next": 1,
        'Language': 'Eng',
        'Version':2.0},
    'Storage': {
        'IDs':[0],
        'List':{
            '0': {'Type':'Charge','Name':'TEST NAME TEST', 
                'Description':'Lorem ipsum et ####','Date':'2137-04-24',
                'Amount':420,'Hidden':False}
        },
        "Budgets":{
            '_': ['main'] #list of budgets
            '0': {
                "Title":"Main",
                "Description": "lorem ipsum bla bla bla"
                "IncludeBudgets":[],
                "Reminders": [min, max],
                "LoT": ['0'] #List of items
            }
        }
    }
}'''

def get_random_id(l:list):
    import random
    offset = 0
    ret = str(random.randrange(0,10))
    while ret in l:
        offset +=5
        ret = str(random.randrange(0+offset,10+offset))
    return ret

def delete(cmd=None):
    log.debug(f'Start of delete function')
    if cmd is None or not len(cmd['args']) == 0:
        print('Arguments not supported')
        return
    get_id = input('ID to be deleted (q to quit): ')
    while True:
        try:
            if get_id =='q':
                return
            if get_id not in Storage["Storage"]['IDs']:
                raise Exception()
        except Exception as ex:
            get_id = input('Please insert correct ID: ')
            continue
        break
    log.debug(f'Gathered id')
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
        log.debug(f'Canceled')
        return
    log.debug(f'Validated')
    Storage['Storage']['IDs'].remove(get_id)
    #STORAGE['Storage']['List'].pop(get_id)
    print('done')
    
def hide(cmd=None):
    log.debug(f'Start hide')
    global Storage
    if cmd is None or not len(cmd['args']) == 0:
        print('Arguments not supported')
        return
    get_id = input('ID to be deleted (q to quit): ')
    while True:
        try:
            if get_id =='q':
                return
            if get_id not in Storage["Storage"]['IDs']:
                raise Exception()
        except Exception as ex:
            get_id = input('Please insert correct ID: ')
            continue
        break
    log.debug(f'Gathered id')
    Storage['Storage']['List'][get_id]['Hidden']=True
    log.debug(f'Hidded')

def list_element(element,id,types='all',hid=True):
    log.debug(f'list element start')
    log.debug(f'{element}')
    if element is None or (element['Hidden']==True and hid ):
        return
    if hid:
        if element['Type'] == 'Charge' and types in ('all','corech','ch','rech','coch'):
            print(f''' {id:4}  | {element["Name"]:25} | {     element["Amount"]:6} | {element["Date"]:10} | {element["Description"]:20}''')
        elif element['Type'] == 'Comment' and types in ('all','corech','coch','core','co'):
            print(f''' {id:4}  | {element["Name"]:25} | {'-----'               :6} | {element["Date"]:10} | {element["Description"]:20}''')
        elif element['Type'] == 'Return' and types in ('all','corech','rech','core','re'):
            print(f''' {id:4}  | {element["Name"]:25} | {element["Amount"]*(-1):6} | {element["Date"]:10} | {element["Description"]:20}''')
    else:
        if element['Hidden'] == False:
            status = ' '
        else:
            status = 'H'
        if element['Type'] == 'Charge' and types in ('all','corech','ch','rech','coch'):
            print(f''' {id:4} {status}| {element["Name"]:25} | {element["Amount"]     :6} | {element["Date"]:10} | {element["Description"]:20}''')
        elif element['Type'] == 'Comment' and types in ('all','corech','coch','core','co'):
            print(f''' {id:4} {status}| {element["Name"]:25} | {'-----'               :6} | {element["Date"]:10} | {element["Description"]:20}''')
        elif element['Type'] == 'Return' and types in ('all','corech','rech','core','re'):
            print(f''' {id:4} {status}| {element["Name"]:25} | {element["Amount"]*(-1):6} | {element["Date"]:10} | {element["Description"]:20}''')

def list_last(cmd=None,n=15):
    log.debug(f'list last start')
    if cmd is None or not len(cmd['args']) == 0:
        print('Arguments not supported')
        log.debug(f'arguments not supported')
        return
    # print(STORAGE)
    sort_list()
    l = Storage['Storage']['IDs']
    l = reversed(l)
    columns_to_be_print = []

    for i in l:
        # print(STORAGE)
        if Storage['Storage']['List'][i]['Hidden']==False:
            log.debug(f'Added to print list: {i}')
            columns_to_be_print.append(i)
            if len(columns_to_be_print) >=n:
                break
    columns_to_be_print = reversed(columns_to_be_print)
    for i in columns_to_be_print:
        log.debug(f'''Listing: {i} {Storage['Storage']['List'][i]}''')
        list_element(Storage['Storage']['List'][i],i)
        
def unhide(cmd=None):
    log.debug(f'started unhide')
    if cmd is None or not len(cmd['args']) == 0:
        print('Arguments not supported')
        log.debug(f'arguments not supported')
        return
    log.debug(f'begin of form')
    get_id = input('ID to be unhided (q to quit): ')
    while True:
        try:
            if get_id =='q':
                return
            if get_id not in Storage["Storage"]['IDs']:
                raise Exception()
        except Exception as ex:
            get_id = input('Please insert correct ID: ')
            continue
        break
    log.debug(f'end of form')
    Storage['Storage']['List'][get_id]['Hidden']=False
    log.debug(f'end of unhide')

def command_not_found(cmd):
    log.debug(f'command not found function')
    print(f"Command not found: {cmd['oryginal']}")

def list_all(cmd=None):
    log.debug(f'list all function start')
    if cmd is None or not len(cmd['args']) == 0:
        print('Arguments not supported')
        log.debug(f'arguments not supported')
        return
    sort_list()
    l = Storage['Storage']['IDs']
    columns_to_be_print = []
    log.debug(f'appending to list to print {15} elements')
    for i in Storage['Storage']['IDs']:
        log.debug(f'{i}')
        columns_to_be_print.append(i)
    # columns_to_be_print = reversed(columns_to_be_print)
    log.debug(f'start iterating')
    for i in columns_to_be_print:
        log.debug(f'printing {i}')
        list_element(Storage['Storage']['List'][i],i,hid=False)

def print_help(cmd = None):
    log.debug(f'help function start')
    print('''
list
*summary
add
delete
hide
unhide
''')
    log.debug('help function ends')
    log.debug(f'{Storage}')

def execute_lst(cmd_list):
    log.debug(f'execute_lst dunction start')
    log.debug(f'call parser')
    parser()
    log.debug(f'comeback from parser')
    log.debug(f'executing list of cmd')
    ret = [execute(cmd) for cmd in cmd_list]
    log.debug(f'end of executong cmds from list')
    log.debug(f'start outer call')
    outer()
    log.debug(f'end outer call')
        
def translate_cmds(cmd):
    log.debug(f'start translate cmds with {cmd}')
    if cmd.lower() in ['a','add']:
        log.debug(f'it is add')
        return 'add'
    elif cmd.lower() in ['de','del','delete','d']:
        log.debug(f'it is delete')
        return 'delete'
    elif cmd.lower() in ['hi','h','hide']:
        log.debug(f'it is hide')
        return 'hide'
    elif cmd.lower() in ['l','li','list','di','ls','sl']:
        log.debug(f'it is list')
        return 'list'
    elif cmd.lower() in ['u','un','unhide']:
        log.debug(f'it is unhide')
        return 'unhide'
    elif cmd.lower() in ['la','all','list_all','listall']:
        log.debug(f'it is list_all')
        return 'list_all'
    elif cmd.lower() in ['h','help']:
        log.debug(f'it is help')
        return 'help'
    elif cmd.lower() in ['s','summary','su']:
        log.debug(f'it is summary')
        return 'summary'
    else:
        log.debug(f'NOT RECOGNIZED')
        return None

def sort_list(asc = True):
    log.debug(f'starting sorting list asc: {asc}')
    l = Storage['Storage']['IDs']
    token = True
    while token:
        token = False
        for i in range(len(l)-1):
            if ( Storage['Storage']['List'][l[i]]['Date']>Storage['Storage']['List'][l[i+1]]['Date'] and asc) or \
               ( Storage['Storage']['List'][l[i]]['Date']<Storage['Storage']['List'][l[i+1]]['Date'] and not asc) :
                l[i],l[i+1] = l[i+1],l[i]
                token = True
    Storage['Storage']['IDs']=l
    log.debug(f'ended sorting list with l: {l}')

def text_terminal():
    log.debug(f'started text_terminal function')
    while True:
        log.debug(f'begin of while')
        command = input('Terminal ~ ')
        if command == '': 
            log.debug(f'blank command')
            continue
        if command.split()[0].lower() in ('q','quit','end','e'):
            log.debug(f'quit fetched')
            break
        else:
            command_split = command.split()
            cmd = [{'type': translate_cmds(command_split[0]),
                   'oryginal': command,
                   'args': command_split[1:]}]
            #print('###',cmd,(cmd[0] is not None ),(not len(cmd[0]['args']) == 0))
            log.debug(f'get command: {cmd}')
            execute_lst(cmd)

def is_linux():
    return sys.platform in [ 'linux' , 'linux2' ]


def clear():
    pass

def summary():
    log.debug('start summary')
    s = 0.0
    a = 0.0
    
    for i in Storage['Storage']['IDs']:
        element = Storage['Storage']['List'][i]
        if element['Type'] == 'Charge':
            
            a += element['Amount']
        elif element['Type'] == 'Return':
            s+=element['Amount']
            
    print(f'''\

    Sum: {s-a}
    
    Abs: {a+s}
    In : {s}
    Out: {a}\n''')
    log.debug('end summary')

if __name__ == '__main__':
    log.debug(f'Start main')
    try:
        text_terminal()
    except Exception as ex:
        log.error(ex)
        print(ex)
        raise ex








'''
{
    'Settings':
        {"ID_next": 1,
        'Language': 'Eng',
        'Version':1.0},
    'Storage': {
        'IDs':[0],
        'List':{
            0: {'Type':'Charge','Name':'TEST NAME TEST', 
                'Description':'Lorem ipsum et ####','Date':'2137-04-24',
                'Amount':420,'Hidden':False}
        }
    }
}'''