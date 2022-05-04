# HV Tools

Really short functions I use all the time. All of these already have widely-used solutions available. These are just my quick-and-dirty functions.

## Installation

From your shell of choice, run

```bash
pip install git+https://github.com/HarryVeilleux/hvtools.git
```

## Usage

In Python environment, run

```python
import hvtools
```

Everything is a function defined in \_\_init\_\_.py, so import explicitly if you want.

### input_to_list

Call x = input_to_list(), type your values (or paste with line breaks separating), and x is a list of strings that you input. Nice to avoid having to wrap everything in quotes when declaring x.

I mostly use this by selecting a full Excel column, copying it, then pasting that into the call.

### csv_to_list

Reads a csv into a list of one element per row. Elements are lists if the given row has a comma, strings otherwise.

### list_to_csv

Writes list of strings, lists, or tuples to csv file with one element per row. Does not (yet) capture commas within strings, so do your own cleanup before using.

This function tests 3x faster than csv.writer for simple lists. Speed is achieved by sacrificing nearly all flexibility.

### json_to_dict

Reads a JSON file into a dictionary. Specify key/keys to subset the return. Set ignore_fnf = True to return empty dictionary instead of raising FileNotFoundError if file does not exist. Set ignore_missing = False to raise KeyError instead of returning None for missing keys.

### dict_to_json

Dumps a dictionary into a JSON file with indent=4. Overwrites without warning.
