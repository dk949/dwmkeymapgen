from parser import _tokens as t
from parser import _keywords as k
from parser import _repeats as rep
from pyleri import Choice, Keyword

# Modkey = Choice(rep.Key, k.ShiftMask, k.ControlMask, *[Keyword(f"Mod{i}Mask") for i in range(1,6)])
