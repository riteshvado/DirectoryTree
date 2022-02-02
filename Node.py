class Node:
    def __init__(self,data):
        self.data=data
        self.parent=None
        self.children=[]


    def addChild(self,childNode):
        ##Childs parent would be self .
        # if childNode is None:
        #     return None
        childNode.parent=self
        #Adding this child as parents children
        self.children.append(childNode)
        return childNode


    def addChildren(self,children=[]):
        for chNode in children:
            self.addChild(chNode)