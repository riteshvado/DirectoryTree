# DirectoryTree

The aim of the project is to build tree representation of directory structure in OS
The tree must also in include all sub dirs. 
We will be using our own Node structure and would build Tree and traverse to print and search within.

Some other features we will need is to find level of node for printing formatted. 
We will also have a feature of find Node in Tree using DFS.

Class Node : Defines Node structure.
             func : addChild for adding Child node to a node.
             func : addChildren Adding children by iterating over list of nodes. 

Module Tree : Generic Functions to :
               findLevels : 
               findPathToParent : From a node we can traverse back based on looking for parent and capture names of all parents. 
               findInTreeDFS : If we pass a node this function will start looking into children and return Node finding he searchKey and Value. 
               

