from pyleri import Grammar
from parser import grammar


def parse(string: str, grammar: Grammar):
    parsed = grammar.parse(string)
    if parsed.is_valid:
        return parsed
    print(parsed.as_str())
    return parsed
