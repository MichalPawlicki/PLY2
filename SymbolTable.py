#!/usr/bin/python

class Symbol(object):
    
    def __init__(self, name, type):
        self.name = name
        self.type = type

class VariableSymbol(Symbol):

    def __init__(self, name, type, value):
        super(VariableSymbol, self).__init__(name, type)
        self.value = value

class SymbolTable(object):

    def __init__(self, parent, name, type):
        self.parent = parent
        self.symbol = Symbol(name, type)
        self.symbols = {}

    def put(self, name, symbol):
        self.symbols[name] = symbol

    def get(self, name):
        return self.symbols[name]

    def getParentScope(self):
        return self.parent





