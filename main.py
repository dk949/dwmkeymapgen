# dwm keymap generator
# 2020-11-15
# dk949

import fileHandler
import parser
from parser import treeParser


def main():
    filename = fileHandler.parseArgs()
    contents = fileHandler.readFile(filename)
    buttonstruct = fileHandler.findStructSignature("static Button buttons[]", contents)
    keystruct = fileHandler.findStructSignature("static Key keys[]", contents)
    mouse = parser.parse(buttonstruct, parser.grammar.MouseGrammar())
    key = parser.parse(keystruct, parser.grammar.KeyGrammar())

    # IMPORTANT: actually run the parser
    treeParser.view_parse_tree(key)
    for i in treeParser.bindings:
        print(i)
    treeParser.view_parse_tree(mouse)
    print("")

    # Print results from the parser
    for i in treeParser.bindings:
        print(i)

    # print nicely formatted tree
    # import json
    # print(json.dumps(treeParser.view_parse_tree(mouse), indent=2))
    # print(json.dumps(treeParser.view_parse_tree(key), indent=2))


if __name__ == '__main__':
    main()
