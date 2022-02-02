import Tree
import DirTree

if __name__ == '__main__':
    #print("Getting all files with .yaml")
    #TODO Get rid of empty dirs
    n=None
    n=DirTree.buildDirTree(filePath="example_dir",filterFunc=lambda f : f.name.endswith('.yaml'))
    #n = DirTree.buildDirTree(filePath="example_dir/UILibs")
    DirTree.printDirTree(node=n)

    # print("============Getting all files================")
    # n1 = DirTree.buildDirTree(filePath="example_dir")
    # DirTree.printDirTree(node=n1)

    #simpleExample()
