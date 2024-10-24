# ADS

# **Post-order Traversal for File System Deletion**

## **Overview**

This project demonstrates **post-order traversal** applied to a **file system deletion** scenario. In this code, directories (folders) and files are represented as nodes in a binary tree. The task is to recursively delete all the files and subdirectories before deleting the main directory, which follows the **post-order traversal** technique.

The structure of the file system in this project is as follows:
```
           Main (folder)
          /     \
      folder1  folder2
      /    \       \
   file1  file2    file3
```

### **Key Concepts:**
- **Post-order Traversal**: In this traversal method, the left subtree is visited first, followed by the right subtree, and finally the root node (i.e., the parent directory).
- **File System Representation**: Each file or folder is treated as a node in a binary tree.

## **Code Breakdown**

### **Classes and Functions:**

1. **`Node` Class**:
   - Represents a folder or file in the file system.
   - Each node has attributes:
     - `name`: Name of the file or folder.
     - `isfile`: A boolean indicating whether the node is a file (`True`) or a folder (`False`).
     - `left` and `right`: Pointers to the left and right children (subfolders or files).

2. **`post_order` Function**:
   - Performs a **post-order traversal** on the binary tree (file system).
   - Recursively visits the left and right subtrees before deleting the current node (file or folder).
   - Deletes files first and then folders, ensuring that all contents are removed before deleting the parent directory.

3. **`Create_file` Function**:
   - Builds a sample binary tree structure representing the file system.
   - The root node is the "Main" folder, which contains two subfolders: `folder1` and `folder2`. 
   - `folder1` contains two files (`file1` and `file2`), and `folder2` contains one file (`file3`).

### **File System Structure**:

```plaintext
           Main (folder)
          /     \
      folder1  folder2
      /    \       \
   file1  file2    file3
```

This binary tree structure simulates a directory (`Main`) that contains two subdirectories (`folder1` and `folder2`). The files (`file1`, `file2`, `file3`) are represented as leaf nodes.

## **How to Run the Code**

### **Prerequisites**:
- You need to have **Python** installed on your machine.

### **Steps**:

1. Clone or download the repository containing the code.
2. Navigate to the folder where the Python script is located.
3. Run the Python script using the following command:

```bash
python Lab_experiment7_gauravnegi.py
```

### **Expected Output**:

When you run the script, it will perform a post-order traversal on the file system and print the deletion process for each file and folder:

```bash
Deleting file: file1
Deleting file: file2
Deleting folder: folder1
Deleting file: file3
Deleting folder: folder2
Deleting folder: Main
All files and folders have been deleted in the correct order.
```

This output indicates that the traversal correctly deletes the files first, followed by the folders.
