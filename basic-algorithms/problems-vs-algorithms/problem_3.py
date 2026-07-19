"""
Problem 3: Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is 
maximum. Return these two numbers. You can assume that all array elements are 
in the range [0, 9]. The number of digits in both the numbers cannot differ by 
more than 1. You're not allowed to use any sorting function that Python 
provides and the expected time complexity is O(nlog(n)).

You should implement the function body according to the rearrange_digits 
function signature. Use the test cases provided below to verify that your 
algorithm is correct. If necessary, add additional test cases to verify that 
your algorithm works correctly.
"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:        # Descending order
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def rearrange_digits(input_list: list[int]) -> tuple[int, int]:
    """
    Rearrange the digits of the input list to form two numbers such that their 
    sum is maximized.

    This function sorts the input list in descending order and then alternates 
    the digits to form two numbers.

    Args:
    input_list (list[int]): A list of integers to be rearranged.

    Returns:
    tuple[int, int]: A tuple containing two integers formed by rearranging the 
    digits of the input list.
    """
    if len(input_list) == 0:
        return (0, 0)

    if len(input_list) == 1:
        return (input_list[0], 0)

    sorted_digits = merge_sort(input_list)

    num1 = ""
    num2 = ""

    for i in range(len(sorted_digits)):
        if i % 2 == 0:
            num1 += str(sorted_digits[i])
        else:
            num2 += str(sorted_digits[i])

    return (int(num1), int(num2))


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]

    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':

    # Test Case 1: Single element
    test_function(([9], [9, 0]))
    # Pass

    # Test Case 2: Example from problem
    test_function(([1, 2, 3, 4, 5], [531, 42]))
    # Pass

    # Test Case 3: All zeros
    test_function(([0, 0, 0, 0, 0], [0, 0]))
    # Pass

    # Test Case 4: Repeated digits
    test_function(([2, 2, 2, 2, 2], [222, 22]))
    # Pass

    # Test Case 5: Larger input
    test_function(([4, 6, 2, 5, 9, 8], [964, 852]))
    # Fail

    # Test Case 6: Empty list
    test_function(([], [0, 0]))
    # Pass