#!python


class ParseTreeNode(object):
    def __init__(self, data):
        """
        Initialize the tree with user expression(math expression)
        
        Args:
            expression(str): string representation of math expression
        """
        self.data = data
        self.right = None
        self.left = None
    
    def __repr__(self):
        """Return a string representation of this parse tree node."""
        return 'ParseTreeNode({!r})'.format(self.data)
    
    def is_leaf(self):
        """Return True if this node is a leaf (that is operands)."""
        return self.left is None and self.right is None


class ParseTree(object):
    def __init__(self, expression=None):
        """
        Initialize the tree with user expression(math expression)
        
        Args:
            expression(str): string representation of math expression
        """
        self.root = None

        if expression is not None:
            for exp in expression:
                self.insert(exp)
