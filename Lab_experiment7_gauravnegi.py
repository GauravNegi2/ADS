class Node:
    def __init__(self, name, isfile=False):
        self.name = name
        self.isfile = isfile
        self.left = None 
        self.right = None  

def post_order(node):
 
    if node:
        post_order(node.left)
        post_order(node.right)

        if node.isfile:
            print(f"Deleting file: {node.name}")
        else:
            print(f"Deleting folder: {node.name}")

def Create_file():
    root = Node("Main")
    root.left = Node("folder1")
    root.right = Node("folder2")
    root.left.left = Node("file1", isfile=True) 
    root.left.right = Node("file2", isfile=True)
    root.right.right = Node("file3", isfile=True)  
    return root

root = Create_file()
print(f"{post_order(root)}\nAll files and folders have been deleted in the correct order.")

# file system tree:
#           Main (folder)
#          /     \
#      folder1  folder2
#      /    \       \
# file1   file2    file3



