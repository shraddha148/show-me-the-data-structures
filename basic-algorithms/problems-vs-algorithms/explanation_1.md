<!--
Problem 1: Square Root of an Integer

## Reasoning Behind Decisions

I used Binary Search because the search space is sorted.
In each step, the algorithm compares the square of the middle element with the target and searches only the relevant half.
This efficiently finds the floor value of the square root without checking every number.
Edge cases such as 0, 1, and negative numbers are also handled.

## Time Efficiency

The algorithm uses Binary Search, which halves the search space in every iteration.
Time Complexity: O(log n)

This satisfies the expected time complexity for the problem.

## Space Efficiency

The algorithm only uses a few variables (left, right, and mid) regardless of the input size and does not use recursion or any extra data structures.
Space Complexity: O(1)