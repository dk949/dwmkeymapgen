# DWM keymap generator

## What does this do
* Reads the dwm config.h
* Extracts the arrays in which key and mouse bindings are stored
* Parses that array
* Prints the list of bindings to the screen (at least for now)

## Requirements
* Python 3
* [pyleri](https://github.com/transceptor-technology/pyleri) library

## Usage
```shell
python main.py -o path/to/config.h
```
