# Returns properties of a node object as a dictionary:
from pyleri import result


class TreeParser:

    def __init__(self, res: result):
        self._bindings = []
        self._binding = []
        self._tree = {}
        self.res = res
        self._parse_tree()

    def _node_props(self, node, children):
        if hasattr(node.element, 'name'):
            if node.element.name == "rep_click_location" \
                    or node.element.name == "rep_modkey" \
                    or node.element.name == "c_buttons" \
                    or node.element.name == "rep_function" \
                    or node.element.name == "reg_keysym":

                self._binding.append(node.string)
            elif node.element.name == "s_argument":
                self._binding[-1] = self._binding[-1] + f"({node.string.lstrip('.') if node.string != '0' else 'void'})"
                self._bindings.append(self._binding.copy())
                self._binding.clear()
            elif node.element.name == "s_tagKeys":
                self._binding.append(node.string)
                self._bindings.append(self._binding.copy())
                self._binding.clear()

        return {
            # 'start': node.start,
            # 'end': node.end,
            'name': node.element.name if hasattr(node.element, 'name') else None,
            'element': node.element.__class__.__name__,
            'string': node.string,
            'children': children
            }

    # Recursive method to get the children of a node object:
    def _get_children(self, children):
        return [self._node_props(c, self._get_children(c.children)) for c in children]

    # View the parse tree:
    def _parse_tree(self):
        self._bindings.clear()
        start = self.res.tree.children[0] \
            if self.res.tree.children else self.res.tree

        self._tree = self._node_props(start, self._get_children(start.children))

    def getBindings(self):
        return self._bindings

    def getTree(self):
        return self._tree
