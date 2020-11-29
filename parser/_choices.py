from parser import _tokens as t
from parser import _keywords as k
from parser import _repeats as rep
from pyleri import Choice, Keyword

Math = Choice(t.Plus, t.Minus, t.Multiply, t.Divide, t.Not, t.And, t.Or)
Buttons = Choice(*[Keyword(f"Button{i}") for i in range(4)])
HeldKey = Choice(k.Null, rep.Modkey)
# Modkey = Choice(rep.Key, k.ShiftMask, k.ControlMask, *[Keyword(f"Mod{i}Mask") for i in range(1,6)])
