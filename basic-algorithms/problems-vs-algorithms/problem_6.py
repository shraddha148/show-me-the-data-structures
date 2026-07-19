"""
Problem 6: Unsorted Integer Array

In this problem, we will look for smallest and largest integer from a list of 
unsorted integers. The code should run in O(n) time. Do not use Python's 
inbuilt functions to find min and max.

You should implement the function body according to the get_min_max function 
signature. Use the test cases provided below to verify that your algorithm is 
correct. If necessary, add additional test cases to verify that your algorithm 
works correctly.
"""

from typing import Optional

def get_min_max(ints: list[int]) -> Optional[tuple[int, int]]:
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
        ints (list[int]): List of integers

    Returns:
        Optional[tuple[int, int]]: (min, max) or None if list is empty
    """

    if len(ints) == 0:
        return None

    minimum = ints[0]
    maximum = ints[0]

    for num in ints:

        if num < minimum:
            minimum = num

        if num > maximum:
            maximum = num

    return (minimum, maximum)


if __name__ == '__main__':

    # Test Case 1: Empty input list
    print(get_min_max([]))
    # Expected Output: None

    # Test Case 2: Negative and positive numbers
    print(get_min_max([-10, 0, 10, -20, 20]))
    # Expected Output: (-20, 20)

    # Test Case 3: Large range of numbers
    print(get_min_max([1000, -1000, 500, -500, 0]))
    # Expected Output: (-1000, 1000)

    # Test Case 4: Already sorted numbers
    print(get_min_max([1, 2, 3, 4, 5]))
    # Expected Output: (1, 5)

    # Test Case 5: Single element
    print(get_min_max([42]))
    # Expected Output: (42, 42)

    # Test Case 6: All elements same
    print(get_min_max([7, 7, 7, 7]))
    # Expected Output: (7, 7)