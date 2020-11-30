# Returns properties of a node object as a dictionary:
from pyleri import result

bindings = []
binding = []


def node_props(node, children):
    global bindings
    global binding

    if hasattr(node.element, 'name'):
        if node.element.name == "rep_click_location"\
                or node.element.name == "rep_modkey"\
                or node.element.name == "c_buttons"\
                or node.element.name == "rep_function"\
                or node.element.name == "reg_keysym":

            binding.append(node.string)
        elif node.element.name == "s_argument":
            binding[-1] = binding[-1] + f"({node.string.lstrip('.') if node.string != '0' else 'void'})"
            bindings.append(binding.copy())
            binding.clear()
        elif node.element.name == "s_tagKeys":
            binding.append(node.string)
            bindings.append(binding.copy())
            binding.clear()



    return {
        # 'start': node.start,
        # 'end': node.end,
        'name': node.element.name if hasattr(node.element, 'name') else None,
        'element': node.element.__class__.__name__,
        'string': node.string,
        'children': children}


# Recursive method to get the children of a node object:
def get_children(children):
    return [node_props(c, get_children(c.children)) for c in children]


# View the parse tree:
def view_parse_tree(res: result):
    global bindings
    bindings.clear()
    start = res.tree.children[0] \
        if res.tree.children else res.tree
    return node_props(start, get_children(start.children))
