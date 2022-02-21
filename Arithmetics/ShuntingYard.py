from collections import namedtuple
from pprint import pprint as pp

NUM = 'NUMBER'
LEFTPARENTHESES = '('
RIGHTPARENTHESES = ')'
LEFT = 'Left'
RIGHT = 'Right'

class ShuntingYard():
    def __init__(self) -> None:
        self.operatorInfo = namedtuple('OperatorInfo', 'precedence associativeness')
    
        self.ops = {
         '^': self.operatorInfo(precedence=4, associativeness=RIGHT),
         '*': self.operatorInfo(precedence=3, associativeness=LEFT),
         '/': self.operatorInfo(precedence=3, associativeness=LEFT),
         '+': self.operatorInfo(precedence=2, associativeness=LEFT),
         '-': self.operatorInfo(precedence=2, associativeness=LEFT),
         '(': self.operatorInfo(precedence=9, associativeness=LEFT),
         ')': self.operatorInfo(precedence=0, associativeness=LEFT),
         }

    def tokenizeInput(self, inputString = None):    
        if inputString is None:
            inputString = input('expression: ')

        tokens = self.__splitString(inputString)
        return self.__createTokenMap(tokens)
    
    #TODO: Revisit splitting this into functions. Everything I've tried so far has been terrible.
    def doShuntingYard(self, tokenMap):
        rpnResult, operatorStack = [], []
        for token, value in tokenMap:
            if token is NUM:
                rpnResult.append(value)
            elif token in self.ops:
                currentToken, (currentPrecedence, currentAssociativeness) = token, value
                while operatorStack:
                    previousOperator, (previousOperatorPrecendence, previousOperatorAssociativeness) = operatorStack[-1]
                    if (currentAssociativeness == LEFT and currentPrecedence <= previousOperatorPrecendence) or (currentAssociativeness == RIGHT and currentPrecedence < previousOperatorPrecendence):
                        if currentToken != RIGHTPARENTHESES:
                            if previousOperator != LEFTPARENTHESES:
                                operatorStack.pop()
                                rpnResult.append(previousOperator)
                            else:    
                                break
                        else:        
                            if previousOperator != LEFTPARENTHESES:
                                operatorStack.pop()
                                rpnResult.append(previousOperator)
                            else:    
                                operatorStack.pop()
                                break
                    else:
                        break
                if currentToken != RIGHTPARENTHESES:
                    operatorStack.append((token, value))

        while operatorStack:
            previousOperator, (previousOperatorPrecendence, previousOperatorAssociativeness) = operatorStack[-1]
            operatorStack.pop()
            rpnResult.append(previousOperator)
        return rpnResult


    def __splitString(self, string):
        return string.strip().split()

    def __createTokenMap(self, tokens):
        tokenMap = []
        for token in tokens:
            if token in self.ops:
                tokenMap.append((token, self.ops[token]))
            else:    
                tokenMap.append((NUM, token))
        return tokenMap