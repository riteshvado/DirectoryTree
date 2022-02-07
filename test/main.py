from DirectoryTree import DirTree

if __name__ == '__main__':
    n= DirTree.buildDirTree(filePath="test/example_dir", filterFunc=lambda f : f.name.endswith('.yaml'))
    DirTree.printDirTree(node=n)
