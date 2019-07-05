import operator


OPERATIONS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}


class Node:
    def __init__(self):
        self.data = None
        self.left: Node = None
        self.right: Node = None
        self.root: Node = self

    def getLeftChild(self):
        if self.left is None:
            self.left = Node()
            self.left.setRoot(root=self)
        return self.left
    
    def getRightChild(self):
        if self.right is None:
            self.right = Node()
            self.right.setRoot(root=self)
        return self.right

    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right

    def getValue(self):
        return self.data
    
    def setValue(self, data: str):
        self.data = data

    def setRoot(self, root):
        self.root = root

    def getNodeRoot(self):
        return self.root

    def printNode(self, delimiter: str):
        s = self.root.getValue() + delimiter + self.data
        if self.left is not None:
            s += ' ' + self.left.printNode('\\')
        if self.right is not None:
            s += ' ' + self.right.printNode('/')
        return s
     

class TreeParser:    
    def __init__(self, expr: str):
        self._expr = expr
        self.currentNode = Node()
        self.root = self.currentNode

    def build_tree(self):
        for token in self._expr.split():
            if token == '(':
                self.currentNode = self.currentNode.getLeftChild()
            
            elif token in OPERATIONS.keys():
                self.currentNode.setValue(data=token)
                self.currentNode = self.currentNode.getRightChild()
            
            elif token == ')':
                self.currentNode = self.currentNode.getNodeRoot()
            
            elif token not in OPERATIONS.keys():
                self.currentNode.setValue(data=token)
                self.currentNode = self.currentNode.getNodeRoot()

        return self.root
        

class TreeEvaluator:
    def __init__(self):
        pass
    
    def resolve_tree(self, tree: Node):
        leftNode = tree.getLeft()
        rightNode = tree.getRight()

        if leftNode is not None and rightNode is not None:
            op = OPERATIONS[tree.getValue()]
            right_result = self.resolve_tree(rightNode)
            left_result = self.resolve_tree(leftNode)
            result = op(left_result, right_result)
            return result
        else:
            return self.try_to_parse(tree.getValue())
    
    def try_to_parse(self, data: str):
        try:
            return int(data)
        except ValueError:
            return float(data)
        except ValueError:
            return data


        
          

    

