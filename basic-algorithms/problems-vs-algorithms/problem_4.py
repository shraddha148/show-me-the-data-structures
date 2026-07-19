def sort_012(input_list):
    """
    Sort an array containing only 0s, 1s, and 2s in a single traversal.

    Args:
        input_list (list): List to be sorted

    Returns:
        list: Sorted list
    """

    low = 0
    mid = 0
    high = len(input_list) - 1

    while mid <= high:

        if input_list[mid] == 0:
            input_list[low], input_list[mid] = input_list[mid], input_list[low]
            low += 1
            mid += 1

        elif input_list[mid] == 1:
            mid += 1

        else:   # input_list[mid] == 2
            input_list[mid], input_list[high] = input_list[high], input_list[mid]
            high -= 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)

    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":

    # Test Case 1
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])

    # Test Case 2
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

    # Test Case 3
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

    # Additional Test Case 4 (Empty List)
    test_function([])

    # Additional Test Case 5 (Single Element)
    test_function([1])

    # Additional Test Case 6 (All Twos)
    test_function([2, 2, 2, 2])

    # Additional Test Case 7 (Reverse Order)
    test_function([2, 2, 2, 1, 1, 1, 0, 0, 0])