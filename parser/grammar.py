from pyleri import Grammar, Sequence


class MouseGrammar(Grammar):
    from parser import _tokens as t
    from parser import _sequences as s

    START = Sequence(t.Lbrace, s.MouseBindings, t.Rbrace)


class KeyGrammar(Grammar):
    from parser import _tokens as t
    from parser import _sequences as s

    START = Sequence(t.Lbrace, s.KeyBindings, t.Rbrace)
