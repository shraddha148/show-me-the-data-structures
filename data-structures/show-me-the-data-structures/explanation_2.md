## Reasoning Behind Decisions:
A recursive Depth-First Search (DFS) approach is used to traverse the directory structure.
The function starts from the given directory and visits every subdirectory recursively.
If an item is a file and its name ends with the given suffix, its path is added to the result list.
Before searching, the function checks for edge cases such as None values or an invalid directory path to avoid runtime errors.
Time Efficiency:
In the worst case, every file and directory is visited exactly once.
Checking whether a file ends with the required suffix takes O(1) (for a fixed-length suffix).

## Overall Time Complexity: O(n), where n is the total number of files and directories in the given path.

## Space Efficiency:
The result list stores all matching file paths.
The recursive calls use the call stack, whose maximum size depends on the depth of the directory tree.

Overall Space Complexity: O(k + d), where:

k = number of matching files stored in the result list.
d = maximum depth of the directory structure due to recursion.

In the worst case, if all files match the suffix, the space complexity is O(n).