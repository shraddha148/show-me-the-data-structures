"""
Problem 1: Square Root of an Integer

Find the floored square root of a given integer without using any Python libraries.
Expected Time Complexity: O(log n)
"""

def sqrt(number: int) -> int:
    """
    Calculate the floored square root of a number.

    Args:
        number (int): Number to find the square root of.

    Returns:
        int: Floored square root.
    """

    # Edge cases
    if number is None or number < 0:
        return None

    if number == 0 or number == 1:
        return number

    left = 0
    right = number

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == number:
            return mid

        elif mid * mid < number:
            left = mid + 1

        else:
            right = mid - 1

    return right


if __name__ == "__main__":

    # Test Case 1
    print("Pass" if 3 == sqrt(9) else "Fail")      # Expected: Pass

    # Test Case 2
    print("Pass" if 0 == sqrt(0) else "Fail")      # Expected: Pass

    # Test Case 3
    print("Pass" if 4 == sqrt(16) else "Fail")     # Expected: Pass

    # Test Case 4
    print("Pass" if 1 == sqrt(1) else "Fail")      # Expected: Pass

    # Test Case 5
    print("Pass" if 6 == sqrt(27) else "Fail")     # Expected: Fail

    # Additional Edge Case 1 (Negative Number)
    print(sqrt(-4))        # Expected: None

    # Additional Edge Case 2 (Large Number)
    print(sqrt(144))   # Expected: 12