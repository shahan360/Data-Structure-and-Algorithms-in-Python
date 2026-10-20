from os import listdir
from os.path import isfile, join

def printnames(dir):
    for file in sorted(listdir(dir)):
        fullpath = join(dir, file)
        if isfile(fullpath):
            print(file)
        else:
            printnames(fullpath) # Recursive call for subdirectory and this is how DFS explores the tree

if __name__ == "__main__":
    printnames("focus")