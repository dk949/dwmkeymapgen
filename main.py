# dwm keymap generator
# 2020-11-15
# dk949

# importing parser will parse the cli arguments
import parser
import extractor


def main():
    # parser.parse() will return a list of key/mouse bindings dependant on the struct signature and grammar supplied
    mouse = parser.parse("static Button buttons[]", parser.grammar.MouseGrammar())
    key = parser.parse("static Key keys[]", parser.grammar.KeyGrammar())

    extractor.extract_mouse(mouse)
    print("")

    extractor.extract_key(key)


if __name__ == '__main__':
    main()
