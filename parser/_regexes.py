from pyleri import Regex
LetterNumberOrPipe = Regex(r'[a-zA-Z0-9]\|?')
Letter = Regex(r'[a-zA-Z]')
Number = Regex(r'[0-9]')
