class Node:
    """
    This class hold the structure of Node : data, parent and children

    """
    def __init__(self,data):
        self.data=data
        self.parent=None
        self.children=[]


    def addChild(self,childNode):
        """
        
        Args:
            childNode (Node): An Node you want to add as child.
        Returns
             Node: The same node after adding to parent node.

        """
        # Child's parent would be self .
        childNode.parent=self
        #Adding this child as parents children
        self.children.append(childNode)
        return childNode


    def addChildren(self,children=[]):
        """
        Convenient method to multiple child nodes to a Node.

        Args:
            children (list): list of child nodes.

        Returns:
            None

        """
        for chNode in children:
            self.addChild(chNode)