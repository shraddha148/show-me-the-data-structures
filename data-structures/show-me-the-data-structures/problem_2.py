import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Args:
        suffix(str): suffix of the file name to be found
        path(str): path of the file system

    Returns:
        list: List of matching file paths
    """
    result = []

    # Edge cases

    if suffix is None or path is None:
        return result

    if not os.path.exists(path):
        return result

    def search(current_path):
        for item in os.listdir(current_path):

            item_path = os.path.join(current_path, item)

            if os.path.isdir(item_path):
                search(item_path)

            elif os.path.isfile(item_path):
                if item.endswith(suffix):
                    result.append(item_path)

    search(path)

    return result

print("Test Case 1")
print(find_files(".h", "./testdir"))

print("Test Case 2")
print(find_files("", "./testdir"))

print("Test Case 3")
print(find_files(".c", "./invalid_directory"))

print(find_files(".java", "./testdir"))  #Additional test case


import os

## Let us print the files in the directory in which you are running this script
print(os.listdir("."))

## Let us check if this file is indeed a file!
print(os.path.isfile("./ex.py"))

## Does the file end with .py?
print("./ex.py".endswith(".py"))
