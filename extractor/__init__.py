from parser import treeParser


# keyBindings[] holds:
#   binding[] which hold:
#       mod key,
#       key pressed,
#       function to be called(args to function)

def extract(tree):
    tokens = treeParser.view_parse_tree(tree)

