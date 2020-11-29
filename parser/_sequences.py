from pyleri import Sequence
from parser import _tokens as t, _repeats as rep

Array = Sequence(t.LsquareBracket, rep.Numbers, t.RsquareBracket)
