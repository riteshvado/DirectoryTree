# DirectoryTree

The aim of the project is to build tree representation of directory structure in OS.  The tree must also in include all sub dirs. 
We will be using our own Node structure and would build Tree and traverse to print and search within.


Class Node : Defines Node structure.
             
             addChild for adding Child node to a node.
             
             addChildren Adding children by iterating over list of nodes. 

Module Tree : Generic Functions to :
               
               findLevels 
               
               findPathToParent : From a node we can traverse back based on looking for parent and capture names of all parents. 
               
               findInTreeDFS : If we pass a node to this function it will start looking into children and return Node finding the searchKey and searchVal.
               
               

