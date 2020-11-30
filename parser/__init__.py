from pyleri import Grammar
from parser import grammar
from parser.treeParser import TreeParser


def parse(string: str, bindingGrammar: Grammar):
    parsed = bindingGrammar.parse(string)
    if parsed.is_valid:
        parsed_list = TreeParser(parsed)
        return parsed_list.getBindings()
    print(parsed.as_str())
    return None
