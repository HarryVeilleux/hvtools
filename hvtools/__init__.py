import json
import pyautogui
import time
from typing import Any, List, Sequence

def csv_to_list(infile: str) -> List[List[str]]:
    """
    Parse contents of csv into list of strings (if one value per row) or lists
        (if multiple).
    """
    with open(infile,'r') as f:
        return [r.split(',') if ',' in r else r for r in f.read().split('\n') if r]

def list_to_csv(outlist: Sequence[Sequence[str]], outfile: str) -> int:
    """Write sequence of strings (or sequence of sequences of strings) to csv file."""
    if len(rlens:=set(len(r) for r in outlist)) > 1:
        rlen=max(rlens)
        outlist = ((',').join(r+['']*(rlen-len(r))) for r in outlist)
    with open(outfile,'w+') as f:
        return f.write(('\n').join([r if isinstance(r,str) else (',').join(r) for r in outlist]))

def json_to_dict(infile: str, key: str = '', keys: Sequence[str] = [],
                 ignore_fnf: bool = True, ignore_missing: bool = False) -> Any:
    """
    Parse contents of JSON file into Python dictionary.
    key: Return value of key in JSON (return None if ignore_missing = True and key not
        in JSON).
    keys: Return dict of keys and values in JSON (return key:None if
        ignore_missing = True and key not in JSON).
    ignore_fnf: Return {} if JSON file does not exist.
    """
    try:
        with open(infile, 'r') as f:
            d = json.load(f)
    except FileNotFoundError:
        if ignore_fnf:
            d = {}
        else:
            raise
    if key:
        if ignore_missing:
            return d.get(key)
        else:
            return d[key]
    elif keys:
        if ignore_missing:
            return {k: d.get(k) for k in keys}
        else:
            return {k: d[k] for k in keys}
    else:
        return d

def dict_to_json(outdict: dict, outfile: str) -> int:
    """Dump Python dictionary into JSON file (overwrites existing)."""
    with open(outfile, 'w+') as f:
        return f.write(json.dumps(outdict,indent=4))

def input_to_list() -> List[str]:
    """Generate list of non-empty user inputs."""
    def prompt():
        while next_el:=input():
            yield next_el
    return list(prompt())

def wake(wtime: int = 150) -> None:
    """Alternate volumeup/volumedown key presses."""
    while True:
        pyautuogui.press('volumeup')
        time.sleep(wtime)
        pyautogui.press('volumedown')
        time.sleep(wtime)
