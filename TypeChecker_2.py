#!/usr/bin/python

from SymbolTable import *

ttype = {}
arithm_ops = [ '+', '-', '*', '/', '%' ]
bit_ops = [ '|', '&', '^', '<<', '>>' ]
log_ops = [ '&&', '||' ]
comp_ops = [ '==', '!=', '>', '<', '<=', '>=' ]
ass_op = ['=']

for op in arithm_ops + bit_ops + log_ops + ass_op:
    ttype[op] = {}
    for type_ in ['int', 'float', 'string']:
        ttype[op][type_] = {}

for arithm_op in arithm_ops:
    ttype[arithm_op]['int']['int'] = 'int'
    ttype[arithm_op]['int']['float'] = 'float'
    ttype[arithm_op]['float']['int'] = 'float'
    ttype[arithm_op]['float']['float'] = 'float'
ttype['+']['string']['string'] = 'string'
ttype['*']['string']['int'] = 'string'
ttype['=']['float']['int'] = 'float'
ttype['=']['float']['float'] = 'float'
ttype['=']['int']['int'] = 'int'
ttype['=']['string']['string'] = 'string'

for op in bit_ops + log_ops:
    ttype[op]['int']['int'] = 'int'

for comp_op in comp_ops:
    ttype[arithm_op]['int']['int'] = 'int'
    ttype[arithm_op]['int']['float'] = 'int'
    ttype[arithm_op]['float']['int'] = 'int'
    ttype[arithm_op]['float']['float'] = 'int'
    ttype[arithm_op]['string']['string'] = 'int'

class IncompatibleTypesError(Exception):
    pass

class DuplicatedSymbolError(Exception):
    pass

class TypeChecker(object):

    def dispatch(self, node, *args):
        self.node = node
        className = node.__class__.__name__
        meth = getattr(self, 'visit_' + className)
        return meth(node, *args)
    
    def findVariable(self, tab, variable):
        if tab.symbols.has_key(variable):
            return tab.get(variable)
        elif tab.getParentScope() != None:
            return self.findVariable(tab.getParentScope(), variable)
        else:
            return None

    def visit_Program(self, node):
        tab = SymbolTable(None, "program")
        self.dispatch(node.declarations, tab)
        self.dispatch(node.fundefs, tab)
        self.dispatch(node.instructions, tab)

    def visit_Declarations(self, node, tab):
        for declaration in node.declarations:
            self.dispatch(declaration, tab)
            
    def visit_Declaration(self, node, tab):
        self.dispatch(node.inits, tab, node.type)

    def visit_Inits(self, node, tab, type):
        for init in node.inits:
            self.dispatch(init, tab, type)

    def visit_Init(self, node, tab, type):
        for symbol in tab.symbols:
            if symbol.id == node.id:
                print "Duplicated usage of symbol {0} in line {1}".format(node.id, node.line)
                raise DuplicatedSymbolError
            else:
                tab.put(VariableSymbol(node.id, type, node.expression))

    def visit_Instructions(self, node, tab):
        for instruction in node.instructions:
            self.dispatch(instruction, tab)
 
    def visit_Instruction(self, node, tab):
        pass

    def visit_Print(self, node, tab):
        self.dispatch(node.expression, tab)

    def visit_Labeled(self, node, tab):
        self.dispatch(node.instruction, tab)
        
    def visit_Assignment(self, node, tab):
        variable = self.findVariable(tab, node.id)
        if variable == None:
            print "Symbol {0} in line {1} not defined before".format(node.id, node.line)
        else:
            valueType = self.dispatch(node.expression)
            if not ttype["="][variable.type].has_key(valueType):
                print "Value of type {0} cannot be assigned to symbol {1} of type {2} (line {3})".format(valueType, node.id, variable.type, node.line)
        
    def visit_Choice(self, node, tab):
        pass

    def visit_If(self, node, tab):
        pass

    def visit_Else(self, node, tab):
        pass

    def visit_While(self, node, tab):
        pass

    def visit_RepeatUntil(self, node, tab):
        pass

    def visit_Return(self, node, tab):
        pass

    def visit_Continue(self, node, tab):
        pass

    def visit_Break(self, node, tab):
        pass

    def visit_Compound(self, node, tab):
        pass

    def visit_Const(self, node, tab):
        value = node.value
        return (type(value) is int and 'int') or \
                (type(value) is float and 'float') \
                or 'string'

    def visit_Id(self, node, tab):
        pass

    def visit_BinExpr(self, node, tab):
        try:
            type1 = self.dispatch(node.expr1)
            type2 = self.dispatch(node.expr2)
            op = node.operator;
            return ttype[op][type1][type2]
        except KeyError:
            print "Incompatible types in line", node.line
            raise IncompatibleTypesError
        except IncompatibleTypesError:
            raise IncompatibleTypesError

    def visit_ExpressionInParentheses(self, node, tab):
        expression = node.expression
        return self.dispatch(expression)

    def visit_ExpressionList(self, node, tab):
        pass

    def visit_FunctionDefinitions(self, node, tab):
        pass

    def visit_FunctionDefinition(self, node, tab):
        pass
    
    def visit_ArgumentList(self, node, tab):
        pass

    def visit_Argument(self, node, tab):
        pass
    
    #def visit_Float(self, node):
    # ... 
    # 

    # ... 
    # 


