# dwm keymap generator
# 2020-11-15
# dk949

import fileHandler
import parser


def main():
    filename = fileHandler.parseArgs()
    contents = fileHandler.readFile(filename)
    buttonstruct = fileHandler.findStructSignature("static Button buttons[]", contents)
    keystruct = fileHandler.findStructSignature("static Key keys[]", contents)
    mouse = parser.parse(buttonstruct, parser.grammar.MouseGrammar())
    key = parser.parse(keystruct, parser.grammar.KeyGrammar())

    for i in mouse:
        print(i)

    print("")

    # Print results from the parser
    for i in key:
        print(i)


if __name__ == '__main__':
    main()
