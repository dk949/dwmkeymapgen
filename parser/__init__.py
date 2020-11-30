from pyleri import Grammar

import fileHandler
from parser import grammar
from parser.treeParser import TreeParser

filename = fileHandler.parseArgs()


def parse(structSignature: str, bindingGrammar: Grammar) -> list:
    contents = fileHandler.readFile(filename)
    struct = fileHandler.findStructSignature(structSignature, contents)
    parsed = bindingGrammar.parse(struct)
    if parsed.is_valid:
        parsed_list = TreeParser(parsed)
        return parsed_list.getBindings()
    print(parsed.as_str())
    return []
