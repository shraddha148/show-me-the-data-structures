"""
Problem 2: Search in a Rotated Sorted Array
"""

def rotated_array_search(input_list: list[int], number: int) -> int:
    """
    Find the index by searching in a rotated sorted array.

    Args:
        input_list (list[int]): Input array to search.
        number (int): Target number to find.

    Returns:
        int: Index of target if found, otherwise -1.
    """

    # Edge case
    if len(input_list) == 0:
        return -1

    left = 0
    right = len(input_list) - 1

    while left <= right:

        mid = (left + right) // 2

        if input_list[mid] == number:
            return mid

        # Left half is sorted
        if input_list[left] <= input_list[mid]:

            if input_list[left] <= number < input_list[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Right half is sorted
        else:

            if input_list[mid] < number <= input_list[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# Test function
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]

    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


if __name__ == '__main__':

    # Test Case 1 (Empty List)
    test_function([[], 5])
    # Expected: Pass

    # Test Case 2 (Beginning)
    test_function([[4, 5, 6, 7, 0, 1, 2], 4])
    # Expected: Pass

    # Test Case 3 (End)
    test_function([[4, 5, 6, 7, 0, 1, 2], 2])
    # Expected: Pass

    # Test Case 4 (Middle)
    test_function([[4, 5, 6, 7, 0, 1, 2], 6])
    # Expected: Pass

    # Additional Test Case 5 (Not Present)
    test_function([[4, 5, 6, 7, 0, 1, 2], 10])
    # Expected: Pass

    # Additional Test Case 6 (Single Element)
    test_function([[-1], 1])
    # Expected: Pass