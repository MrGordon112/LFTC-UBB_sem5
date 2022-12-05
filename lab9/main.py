from FiniteAutomata import FiniteAutomata
from Grammar import Grammar
from Parser import Parser

from Scanner import Scanner

if __name__ == '__main__':
    # scanner = Scanner()
    # st, pif, message = scanner.scan("input/Lab1a - p3.txt")
    # fa = FiniteAutomata('input/constant-integer.in')
    # fa.start()

    parser = Parser("input/g2.txt")
    # grammar=Grammar("input/g1.txt")
    # grammar.start()

    parser.toStringCanonicalCollection()
