from pyleri import Grammar, Sequence, Regex, Repeat, Keyword, Token, Choice, Optional
from pyleri.elements import Element


class MouseGrammar(Grammar):
    t_lbrace = Token('{')
    t_rbrace = Token('}')
    t_lsquareBracket = Token('[')
    t_rsquareBracket = Token(']')
    t_comma = Token(',')
    t_dot = Token('.')
    t_equals = Token('=')
    t_plus = Token('+')
    t_minus = Token('-')
    t_multiply = Token('*')
    t_divide = Token('/')
    t_not = Token('~')
    t_and = Token('&')
    t_or = Token('|')

    k_null = Keyword('0')

    reg_letterNumberOrPipe = Regex(r'[a-zA-Z0-9]\|?')
    reg_letter = Regex(r'[a-zA-Z]')
    reg_number = Regex(r'[0-9]')

    rep_numbers = Repeat(reg_number, 1, None)
    rep_click_location = Repeat(reg_letter, 1, None)
    rep_modkey = Repeat(reg_letterNumberOrPipe, 1, None)
    rep_function = Repeat(reg_letter, 1, None)

    c_math = Choice(t_plus, t_minus, t_multiply, t_divide, t_not, t_and, t_or)
    c_buttons = Choice(*[Keyword(f"Button{i}") for i in range(4)])

    s_array = Sequence(t_lsquareBracket, rep_numbers, t_rsquareBracket)
    s_argument = Repeat(Choice(t_dot, k_null, c_math, s_array, rep_function, t_equals, reg_number), 0, None)
    s_mouseBinding = Sequence(t_lbrace, rep_click_location, t_comma,
                              rep_modkey, t_comma, c_buttons,
                              t_comma, rep_function, t_comma, t_lbrace,
                              s_argument, t_rbrace, t_rbrace)
    s_mouseBindings = Repeat(Sequence(s_mouseBinding, Optional(t_comma)), 0, None)
    START = Sequence(t_lbrace, s_mouseBindings, t_rbrace)


class KeyGrammar(Grammar):
    t_lbrace = Token('{')
    t_rbrace = Token('}')
    t_lsquareBracket = Token('[')
    t_rsquareBracket = Token(']')
    t_lbracket = Token('(')
    t_rbracket = Token(')')
    t_comma = Token(',')
    t_dot = Token('.')
    t_equals = Token('=')
    t_plus = Token('+')
    t_minus = Token('-')
    t_multiply = Token('*')
    t_divide = Token('/')
    t_not = Token('~')
    t_and = Token('&')
    t_or = Token('|')

    k_null = Keyword('0')

    reg_letterNumberOrPipe = Regex(r'[a-zA-Z0-9]\|?')
    reg_letter = Regex(r'[a-zA-Z]')
    reg_number = Regex(r'[0-9]')
    reg_keysym = Regex(r'XK_[a-zA-Z0-9]+')

    rep_numbers = Repeat(reg_number, 1, None)
    rep_modkey = Repeat(reg_letterNumberOrPipe, 1, None)
    rep_function = Repeat(reg_letter, 1, None)
    rep_tagkeysFunction = Repeat(reg_letter, 1, None)

    c_math = Choice(t_plus, t_minus, t_multiply, t_divide, t_not, t_and, t_or)

    s_array = Sequence(t_lsquareBracket, rep_numbers, t_rsquareBracket)
    s_argument = Repeat(Choice(t_dot, k_null, c_math, s_array, rep_function, t_equals, reg_number), 0, None)
    s_modKeyCombo = Repeat(Sequence(rep_modkey, Optional(t_or)), 0, None)
    s_keyBinding = Sequence(t_lbrace, s_modKeyCombo, t_comma, reg_keysym,
                            t_comma, rep_function, t_comma, t_lbrace,
                            s_argument, t_rbrace, t_rbrace)
    s_tagKeys = Sequence(rep_tagkeysFunction, t_lbracket, reg_keysym, t_comma, reg_number, t_rbracket)
    s_keyBindings = Repeat(Sequence(Choice(s_keyBinding, s_tagKeys), Optional(t_comma)))
    START = Sequence(t_lbrace, s_keyBindings, t_lbrace)
