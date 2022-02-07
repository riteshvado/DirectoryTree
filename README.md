# DirectoryTree

The aim of the project is to build tree representation of directory structure in OS. The tree must also in include all
sub dirs. We will be using our own Node structure and would build Tree and traverse to print and search within. The
module will also allow capability to filter directories by properties of files like :
Refer attributes of https://docs.python.org/3/library/os.html#os.DirEntry
--'is_file'

--'is_symlink' :

--'name'

--'path'

--'stat' : os.DirEntry.stat(*, follow_symlinks = True)

Module DirTree : This would be the main module that will be used.

       buildDirTree :  Create tree structure of dir and files. 
                       Tree can also be filtered by passing a function which can operate on os.DirEntry (https://docs.python.org/3/library/os.html#os.DirEntry) as its input.
                       Examples : buildDirTree(filePath="example_dir",filterFunc=lambda f : f.name.endswith('.yaml'))

                      
               
       printDirTree : This is for pretty printing of tree.


Example of tree filtered by extension as yaml:

![Example of tree filtered by extension as yaml](/images/image_with_file_filter_as_yaml_extension.JPG)

Example of entire Tree no filter:

![Example of entire Tree no filter](/images/image_without_file_filter.JPG)



Class Node : Defines Node structure.

      addChild for adding Child node to a node.
             
      addChildren Adding children by iterating over list of nodes. 

Module Tree : Generic Functions to :

       findLevels : Finds the depth of Node : Number of edges from Node to Root.  
               
       findPathToParent : From a node we can traverse back based on looking for parent and capture names of all parents. 
               
       findInTreeDFS : If we pass a node to this function it will start looking into children and return Node finding the searchKey and searchVal.
               
               

