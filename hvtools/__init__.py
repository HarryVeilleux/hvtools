from pyautogui import press
from time import sleep

def awake(wtime=150):
    """
    Keeps your computer awake by alternating volumeup/volumedown key presses
    REMEMBER: Snitches get stitches
    """
    while True:
        press('volumeup')
        sleep(wtime)
        press('volumedown')
        sleep(wtime)

def csv_to_list(infile):
    """Read .csv into as list of tuples (or simple list if one value/row)"""
    with open(infile,'r') as f:
        raw_rows = [r.split(',') for r in f.read().split('\n') if r]
    raw_lengths = set([len(r) for r in raw_rows])
    if any([l>1 for l in raw_lengths]):
        return raw_rows
    else:
        return [r[0] for r in raw_rows]

def list_to_csv(wlist, outfile):
    """
    Writes Python list of lists, tuples, or characters to csv file, one
        element per row
    Extremely restricted input compared to csv.writer, but faster when useable
    """
    if isinstance(wlist[0],list) or isinstance(wlist[1],tuple):
        wlist = [(',').join([str(el) for el in r]) for r in wlist]
    else:
        wlist = [str(el) for el in wlist]
    with open(outfile,'w+') as f:
        return f.write(('\n').join(wlist))

def input_to_list():
    """Prompts user to input values and returns all as list"""
    rlist = []
    while True:
        el = input('')
        if not el:
            return rlist
        else:
            rlist.append(el)
