from pyleri import Repeat
from parser import _regexes as reg

Numbers = Repeat(reg.Number, 1, None)

Click_location = Repeat(reg.Letter, 1, None)
Modkey = Repeat(reg.LetterNumberOrPipe, 1, None)
Function = Repeat(reg.Letter, 1, None)
TagkeysFunction = Repeat(reg.Letter, 1, None)
