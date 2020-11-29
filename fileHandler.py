import re
import string
import sys


def parseArgs():
    if "-o" in sys.argv:
        try:
            filename = sys.argv[sys.argv.index("-o") + 1]
            del sys.argv[sys.argv.index("-o") + 1]
            del sys.argv[sys.argv.index("-o")]
        except IndexError:
            print("please supply the location of the file to open")
            sys.exit(1)
    else:
        print("-o option with the file location of the file to open is required")
        sys.exit(1)
    return filename


def readFile(filename: str):
    with open(filename, "r") as f:
        contents = f.read()
    return contents


def _removeComments(contents: str):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " "  # note: a space and not an empty string
        else:
            return s

    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, contents)


def _stripUntilBrace(contents):
    contents = list(contents)
    while not contents[0] == '{':
        del contents[0]
    return ''.join(contents)


def _extractBindings(start: str, contents: str) -> str:
    binding_start = contents.find(start) + len(start)
    binding_end = contents[binding_start:].find(";") + binding_start
    return _stripUntilBrace(contents[binding_start:binding_end])


def _removeWhiteSpace(contents: str):
    return contents.translate({ord(c): None for c in string.whitespace})


def findStructSignature(signature: str, contents: str) -> str:
    return _extractBindings(_removeWhiteSpace(signature), _removeWhiteSpace(_removeComments(contents)))
