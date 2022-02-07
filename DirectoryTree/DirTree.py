import os
from DirectoryTree.Node import Node
from DirectoryTree import Tree

def buildDirTree(filePath=None,filterFunc=lambda f : True,parentPath=[]):
    """

    Args:
        filePath (str): filepath as string.
        filterFunc: You can create a function and pass it reference.
        The function will have os.DirEntry as its input (https://docs.python.org/3/library/os.html#os.scandir,https://docs.python.org/3/library/os.html#os.DirEntry)
        This input can be further handled by function to filter certain files.
        Example : buildDirTree(filePath="example_dir",filterFunc=lambda f : f.name.endswith('.yaml'))

        parentPath: System Manages this.

    Returns: Tree

    """
    flag=False
    baseName = os.path.basename(filePath)
    tmp=None
    with os.scandir(filePath) as f:
        for i in f:
            if i.is_file():
                if filterFunc(i):
                    if flag is False:
                        tmp = Node({"name": baseName, 'type': 'DIR'})
                        parentPath.append(tmp.data['name'])
                        flag=True

                    tmp.addChild( Node({ 'name' : i.name
                                            , 'type' : "FILE"
                                            , 'filePath' : "--> ".join(parentPath)
                                            , 'size' : i.stat(follow_symlinks=False).st_size}) )
            elif i.is_dir():
                ##If the file is dir. We want to check if matching files are there before making node for its parent.
                #If matching file found that block will create the node and flag=True
                ##And we move to the next
                _chNode=buildDirTree(filePath=i.path,parentPath=parentPath.copy(),filterFunc=filterFunc)
                if _chNode:
                    if flag is False:
                        tmp = Node({"name": baseName, 'type': 'DIR'})
                        parentPath.append(tmp.data['name'])
                        flag = True
                    tmp.addChild(_chNode)

    return tmp




def printDirTree(node=None,indent=1):
    """
    Prints tree in more readable way
    Args:
        node: Node from which you want to start
        indent: 1  

    Returns: None

    """
    if node is None:
        print("Tree is empty")
        return
    else:
        if node.data['type'] == 'FILE':
            color= Tree.bgcolors.GREEN
            print(color +"|_" +"_" * Tree.findLevels(node=node) * indent, node.data)
        elif node.data['type'] == 'DIR' and bool(node.children) is True:
            color = Tree.bgcolors.BLUE
            print(color + "|_" + "_" * Tree.findLevels(node=node) * indent, node.data)

        for child in node.children:
            printDirTree(child)


