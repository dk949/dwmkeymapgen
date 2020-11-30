# dwm keymap generator
# 2020-11-15
# dk949

import parser


def main():

    mouse = parser.parse("static Button buttons[]", parser.grammar.MouseGrammar())
    key = parser.parse("static Key keys[]", parser.grammar.KeyGrammar())

    for i in mouse:
        print(i)

    print("")

    for i in key:
        print(i)


if __name__ == '__main__':
    main()
