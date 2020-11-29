from pyleri import Sequence, Repeat, Choice, Optional

from parser import _tokens as t
from parser import _repeats as rep
from parser import _choices as c
from parser import _keywords as k
from parser import _regexes as reg

Array = Sequence(t.LsquareBracket, rep.Numbers, t.RsquareBracket)
Argument = Repeat(Choice(t.Dot, k.Null, c.Math, Array, rep.Function, t.Equals, reg.Number), 0, None)
ModKeyCombo = Repeat(Sequence(rep.Modkey, Optional(t.Or)), 0, None)

MouseBinding = Sequence(t.Lbrace, rep.Click_location, t.Comma,
                        rep.Modkey, t.Comma, c.Buttons,
                        t.Comma, rep.Function, t.Comma, t.Lbrace,
                        Argument, t.Rbrace, t.Rbrace)

MouseBindings = Repeat(Sequence(MouseBinding, Optional(t.Comma)), 0, None)

KeyBinding = Sequence(t.Lbrace, ModKeyCombo, t.Comma, reg.Keysym,
                      t.Comma, rep.Function, t.Comma, t.Lbrace,
                      Argument, t.Rbrace, t.Rbrace)

TagKeys = Sequence(rep.TagkeysFunction, t.Lbracket, reg.Keysym, t.Comma, reg.Number, t.Rbracket)

KeyBindings = Repeat(Sequence(Choice(KeyBinding, TagKeys), Optional(t.Comma)))

