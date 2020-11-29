from pyleri import Grammar, Sequence, Regex, Repeat, Keyword, Choice, Optional
from parser import _tokens as t, _choices as c, _repeats as rep, _regexes as reg, _sequences as s


class MouseGrammar(Grammar):
    k_null = Keyword('0')

    rep_click_location = Repeat(reg.Letter, 1, None)
    rep_modkey = Repeat(reg.LetterNumberOrPipe, 1, None)
    rep_function = Repeat(reg.Letter, 1, None)
    c_buttons = Choice(*[Keyword(f"Button{i}") for i in range(4)])

    s_argument = Repeat(Choice(t.Dot, k_null, c.Math, s.Array, rep_function, t.Equals, reg.Number), 0, None)
    s_mouseBinding = Sequence(t.Lbrace, rep_click_location, t.Comma,
                              rep_modkey, t.Comma, c_buttons,
                              t.Comma, rep_function, t.Comma, t.Lbrace,
                              s_argument, t.Rbrace, t.Rbrace)
    s_mouseBindings = Repeat(Sequence(s_mouseBinding, Optional(t.Comma)), 0, None)
    START = Sequence(t.Lbrace, s_mouseBindings, t.Rbrace)


class KeyGrammar(Grammar):
    k_null = Keyword('0')

    reg_keysym = Regex(r'XK_[a-zA-Z0-9]+')

    rep_modkey = Repeat(reg.LetterNumberOrPipe, 1, None)
    rep_function = Repeat(reg.Letter, 1, None)

    s_argument = Repeat(Choice(t.Dot, k_null, c.Math, s.Array, rep_function, t.Equals, reg.Number), 0, None)
    s_modKeyCombo = Repeat(Sequence(rep_modkey, Optional(t.Or)), 0, None)
    s_keyBinding = Sequence(t.Lbrace, s_modKeyCombo, t.Comma, reg_keysym,
                            t.Comma, rep_function, t.Comma, t.Lbrace,
                            s_argument, t.Rbrace, t.Rbrace)
    s_tagKeys = Sequence(rep.TagkeysFunction, t.Lbracket, reg_keysym, t.Comma, reg.Number, t.Rbracket)
    s_keyBindings = Repeat(Sequence(Choice(s_keyBinding, s_tagKeys), Optional(t.Comma)))
    START = Sequence(t.Lbrace, s_keyBindings, t.Rbrace)
