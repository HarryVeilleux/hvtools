# HV Tools

Really short functions I use all the time. Most of them barely qualify as beginner Python projects, but I saved them here because I was typing them so often from the command line.

All of these (except awake) have widely-used (and likely better) solutions available. These are just my quick-and-dirty functions that are good enough for government work.

# Installation

From your shell of choice, run

```bash
pip install git+https://github.com/HarryVeilleux/hvtools.git
```

## awake

Keeps your computer awake and tricks some chat apps (Skype, Teams) into thinking you're online by using pyautogui to press volumeup, wait (default 150 seconds), press volumedown, wait, then loop until user exits.

I have only tested this for Skype and Teams. I have no idea if it works for Slack, Google apps, etc. Please let me know if you confirm one way or the other.

Remember, if you tell your boss about this, you're a bad person. If you are a boss, just let your employees vibe okay?

## csv_to_list

Reads a csv into a list of one element per row. Elements are tuples if any row has commas, strings otherwise.

## list_to_csv

Writes list of strings, lists, or tuples to csv file with one element per row. Does not (yet) capture commas within strings, so do your own cleanup before using.

This function tests 3x faster than csv.writer for simple lists. Speed is achieved by sacrificing nearly all flexibility.

## input_to_list

Call x = input_to_list(), type your values (or paste with line breaks separating), and x is a list of strings that you input. Nice to avoid having to wrap everything in quotes when declaring x.

I mostly use this by selecting a full Excel column, copying it, then pasting that into the call.
