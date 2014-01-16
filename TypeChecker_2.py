#!/usr/bin/python

ttype = {}
arithm_ops = [ '+', '-', '*', '/', '%' ]
bit_ops = [ '|', '&', '^', '<<', '>>' ]
log_ops = [ '&&', '||' ]
comp_ops = [ '==', '!=', '>', '<', '<=', '>=' ]

for op in arithm_ops + bit_ops + log_ops:
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

class TypeChecker(object):

    def dispatch(self, node, *args):
        self.node = node
        className = node.__class__.__name__
        meth = getattr(self, 'visit_' + className)
        return meth(node, *args)
    
    def visit_Variable(self, node):
        pass

    def visit_Program(self, node):
        pass

    def visit_Declarations(self, node):
        pass

    def visit_Inits(self, node):
        pass

    def visit_Init(self, node):
        pass

    def visit_Instructions(self, node):
        pass
 
    def visit_Instruction(self, node):
        pass

    def visit_Print(self, node):
        pass

    def visit_Labeled(self, node):
        pass

    def visit_Assignment(self, node):
        pass

    def visit_Choice(self, node):
        pass

    def visit_If(self, node):
        pass

    def visit_Else(self, node):
        pass

    def visit_While(self, node):
        pass

    def visit_RepeatUntil(self, node):
        pass

    def visit_Return(self, node):
        pass

    def visit_Continue(self, node):
        pass

    def visit_Break(self, node):
        pass

    def visit_Compound(self, node):
        pass

    def visit_Const(self, node):
        value = node.value
        return (type(value) is int and 'int') or \
                (type(value) is float and 'float') \
                or 'string'

    def visit_Id(self, node):
        pass

    def visit_BinExpr(self, node):
        try:
            type1 = self.dispatch(node.left)
            type2 = self.dispatch(node.right)
            op = node.op;
            return ttype[op][type1][type2]
        except KeyError:
            print "Incompatible types in line", node.line
            raise IncompatibleTypesError
        except IncompatibleTypesError:
            raise IncompatibleTypesError

    def visit_ExpressionInParentheses(self, node):
        expression = node.expression
        return self.dispatch(expression)

    def visit_ExpressionList(self, node):
        pass

    def visit_FunctionDefinitions(self, node):
        pass

    def visit_FunctionDefinition(self, node):
        pass
    
    def visit_ArgumentList(self, node):
        pass

    def visit_Argument(self, node):
        pass
    
    #def visit_Float(self, node):
    # ... 
    # 

    # ... 
    # 


