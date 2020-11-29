from pyleri import Choice
from parser import _tokens as t
Math = Choice(t.Plus, t.Minus, t.Multiply, t.Divide, t.Not, t.And, t.Or)

