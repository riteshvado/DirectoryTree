from DirectoryTree.BgColors import BgColors as bgcolors


def printTree(node=None,indent=1):
    """
    Prints tree in more redable way
    :param node: Node from which you want to start.
    :param indent:
    :return:
    """
    if node is None:
        print("Tree is empty")
        return
    else:
        color=bgcolors.BLUE
        if bool(node.children) is False:
            color=bgcolors.GREEN
        print(color+"|_"+"_"*findLevels(node=node)*indent,node.data)
        for child in node.children:
            printTree(child)


def findLevels(node=None,level=0):
    """
    This gives you level of each not by bakctracking parent until we read root.
    :param node:
    :param level:
    :return: level int value.
    """
    if node.parent is None:
        return level
    else:
        #Returning from function is important otherwise you get none.
        #print(node.data)
        return findLevels(node=node.parent,level=level+1)



def findPathToParent(node=None,parent=[]):
    """
    From node you can find all its parent. s
    :param node:
    :param parent:
    :return:
    """
    parent.append(node.data.get('name'))
    if node.parent is None:
        return parent
    else:
        return findPathToParent(node=node.parent,parent=parent)

def findInTreeDFS(node=None,searchKey=None,searchVal=None,resNode=None):
    """
    This is depth first search we are making. Recursively calling children of children.
    :param node:
    :param searchKey:
    :param searchVal:
    :param resNode:
    :return:
    """
    print(node.data)
    if node.data is not None:
        if node.data.get(searchKey) == searchVal:
            resNode=node
            print("--found--", resNode)
            return resNode

    for child in node.children:
        if resNode is None:
            ##Here we need to capture the result and pass again as result node so we can have resNode getting passed accross recursive calls.
            resNode=findInTreeDFS(node=child,searchKey=searchKey,searchVal=searchVal,resNode=resNode)
        else:
            ##This will break further recursion
            break

    return resNode