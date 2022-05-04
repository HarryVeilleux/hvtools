import json
import pytest
import random
import string
import hvtools

def rand_csv_row():
    # only letters
    def el():
        return ('').join(random.choices(string.ascii_letters, k=random.randint(0,50)))
    return [el() for i in range(random.randint(0,10))]

def test_list_to_csv_creates(tmp_path):
    assert not (tmp_path / 'test.csv').exists()
    _=hvtools.list_to_csv(['a','b'],tmp_path / 'test.csv')
    assert (tmp_path / 'test.csv').is_file()

def test_list_to_csv_writes_letters(tmp_path):
    assert not (tmp_path / 'test.csv').exists()
    tl = [rand_csv_row() for i in range(random.randint(10,150))]
    mlen = max(len(r) for r in tl)
    tg = (r+['']*(mlen-len(r)) for r in tl)
    _ = hvtools.list_to_csv(tl,tmp_path / 'test.csv')
    assert (tmp_path / 'test.csv').read_text() == ('\n').join([(',').join(r) for r in tg])

def test_list_to_csv_writes_printable(tmp_path):
    # include whitespace, line breaks - string.printable
    pass

def test_csv_to_list_dne(tmp_path):
    with pytest.raises(FileNotFoundError):
        _ = hvtools.csv_to_list(tmp_path / 'test.csv')

def test_csv_to_list_letters(tmp_path):
    tl = [rand_csv_row() for i in range(random.randint(10,150))]
    with (tmp_path / 'test.csv').open('w+') as f:
        _=f.write(('\n').join([(',').join(r) for r in tl]))
    tr = hvtools.csv_to_list(tmp_path / 'test.csv')
    tg = (r[0] if len(r)==1 else r for r in tl)
    assert tr == [r for r in tg if r]

def test_csv_to_list_printable(tmp_path):
    # include whitespace, line breaks - string.printable
    pass

def rand_json():
    def v():
        t = random.choice(['str','num','arr','bool','null'])
        if t=='str':
            return ('').join(random.choices(string.printable,k=random.randint(0,50)))
        elif t=='num':
            return random.randint(0,999999)
        elif t=='arr':
            return [v() for i in range(random.randint(0,10))]
        elif t=='bool':
            return random.choice([True,False])
        elif t=='null':
            return None
    return {str(i):v() for i in range(random.randint(1,20))}

def test_dict_to_json_creates(tmp_path):
    assert not (tmp_path / 'test.json').exists()
    _=hvtools.dict_to_json({'a':'b'},tmp_path / 'test.json')
    assert (tmp_path / 'test.json').is_file()

def test_dict_to_json_writes(tmp_path):
    assert not (tmp_path / 'test.json').exists()
    tj = rand_json()
    _=hvtools.dict_to_json(tj, tmp_path / 'test.json')
    with (tmp_path / 'test.json').open('r') as f:
        assert json.load(f) == tj

def test_json_to_dict_dne_ignore_fnf(tmp_path):
    assert hvtools.json_to_dict(tmp_path / 'test.json') == {}

def test_json_to_dict_dne_do_not_ignore_fnf(tmp_path):
    with pytest.raises(FileNotFoundError):
        _=hvtools.json_to_dict(tmp_path / 'test.json', ignore_fnf=False)

def dump_json(j, p):
    with p.open('w+') as f:
        _=f.write(json.dumps(j,indent=4))

def test_json_to_dict_reads(tmp_path):
    tj = rand_json()
    dump_json(tj, (tmp_path / 'test.json'))
    assert hvtools.json_to_dict(tmp_path / 'test.json') == tj

def test_json_to_dict_key(tmp_path):
    tj = rand_json()
    dump_json(tj, (tmp_path / 'test.json'))
    for k,v in tj.items():
        assert hvtools.json_to_dict(tmp_path / 'test.json', key=k) == v

def test_json_to_dict_keys(tmp_path):
    tj = rand_json()
    dump_json(tj, (tmp_path / 'test.json'))
    assert hvtools.json_to_dict(tmp_path / 'test.json', keys=list(tj.keys())) == tj
    tks = random.choices(list(tj.keys()), k=max(len(tj)-1,1))
    assert hvtools.json_to_dict(tmp_path / 'test.json', keys=tks) == {k:tj[k] for k in tks}

def test_json_to_dict_key_ignore_missing(tmp_path):
    tj = rand_json()
    dump_json(tj, (tmp_path / 'test.json'))
    assert hvtools.json_to_dict(tmp_path / 'test.json', key='INVALID', ignore_missing=True) == None

def test_json_to_dict_key_do_not_ignore_missing(tmp_path):
    tj = rand_json()
    dump_json(tj, (tmp_path / 'test.json'))
    with pytest.raises(KeyError):
        _=hvtools.json_to_dict(tmp_path / 'test.json', key='INVALID', ignore_missing=False)

def test_json_to_dict_keys_ignore_missing(tmp_path):
    tj = rand_json()
    dump_json(tj, (tmp_path / 'test.json'))
    tks = random.choices(list(tj.keys()), k=len(tj)-1)+['INVALID']
    assert hvtools.json_to_dict(tmp_path / 'test.json', keys=tks, ignore_missing=True) == {k:tj.get(k) for k in tks}

def test_json_to_dict_keys_do_not_ignore_missing(tmp_path):
    tj = rand_json()
    dump_json(tj, (tmp_path / 'test.json'))
    tks = random.choices(list(tj.keys()), k=len(tj)-1)+['INVALID']
    with pytest.raises(KeyError):
        _=hvtools.json_to_dict(tmp_path / 'test.json', keys=tks, ignore_missing=False)
