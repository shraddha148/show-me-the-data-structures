<!--
Problem 6: Unsorted Integer Array

# Explanation

## Reasoning Behind Decisions:

I used a single linear traversal of the list while maintaining two variables, minimum and maximum, to keep track of the smallest and largest values encountered. This approach avoids using Python's built-in min() and max() functions and satisfies the required O(n) time complexity. It is simple, efficient, and only requires comparing each element once.

## Time Efficiency:

The algorithm scans the list only once, performing constant-time comparisons for each element. Therefore, the overall time complexity is O(n), where n is the number of elements in the list.

## Space Efficiency:

The algorithm uses only two additional variables (minimum and maximum) regardless of the input size. 
Hence, the space complexity is O(1).