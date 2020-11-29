from pyleri import Grammar
from parser import grammar


def parse(string: str, bindingGrammar: Grammar):
    parsed = bindingGrammar.parse(string)
    if parsed.is_valid:
        return parsed
    print(parsed.as_str())
    return parsed
