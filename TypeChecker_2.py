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

class TypeChecker(object):

    def dispatch(self, node, *args):
        self.node = node
        className = node.__class__.__name__
        meth = getattr(self, 'visit_' + className)
        return meth(node, *args)


    def visit_BinExpr(self, node):
        type1 = self.dispatch(node.left)
        type2 = self.dispatch(node.right)
        op    = node.op;
        # ... 
        #
 
    def visit_RelExpr(self, node):
        type1 = self.dispatch(node.left)
        type2 = self.dispatch(node.right)
        # ... 
        #

    def visit_Integer(self, node):
        return 'int'

    #def visit_Float(self, node):
    # ... 
    # 

    # ... 
    # 


